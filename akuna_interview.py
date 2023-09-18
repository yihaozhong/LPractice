import uuid
from typing import List, Callable, Any

# Assuming 'async' is meant for asynchronous functions.
# If you're not using asyncio or any async framework, we should remove the 'async' keyword.

class AkunaMessage:
    def __init__(self, timestamp_millis: int, topic: str, message_type: str, message: Any):
        self.timestamp_millis = timestamp_millis
        self.topic = topic
        self.message_type = message_type
        self.message = message

class AkunaLiveClient:
    def __init__(self):
        # Assuming you want to maintain a mapping of subscriptions, we can use a dictionary.
        self.subscriptions = {}
    
    async def subscribe(self, topic: str, callback: Callable) -> uuid.UUID:
        subscription_id = uuid.uuid4()
        self.subscriptions[subscription_id] = (topic, callback)
        # Here, you might want to add logic to actually start the subscription, like connecting to a server.
        return subscription_id
    
    async def unsubscribe(self, subscription_id: uuid.UUID) -> bool:
        if subscription_id in self.subscriptions:
            # Here, you might want to add logic to stop the subscription, like disconnecting from a server.
            del self.subscriptions[subscription_id]
            return True
        return False
    
    async def data_callback(self, message: AkunaMessage):
        # Logic to handle the incoming message and invoke the appropriate callback.
        pass

class AkunaHistoricalClient:
    async def get_range(self, topics: List[str], start_millis: int, end_millis: int) -> List[AkunaMessage]:
        # Logic to fetch historical data for the given topics and time range.
        pass


class DAClient:
    def __init__(self):
        self.hist_client = AkunaHistoricalClient()
        self.live_client = AkunaLiveClient()
        self.subscriptions = {}  # { master_sub_id: [live_sub_id1, live_sub_id2, ...] }

    def get_topics(self, message_types: List[str]) -> List[str]:
        topic_mapping = {
            "msg_type_1": ["topic1", "topic2"],
            "msg_type_2": ["topic3", "topic4"],
            # ... add more mappings as needed
        }
        topics = []
        for msg_type in message_types:
            topics.extend(topic_mapping.get(msg_type, []))
        return topics

    async def subscribe(self, message_types: List[str], user_callback: Callable, 
                        error_callback: Callable, start_millis: int = None, 
                        end_millis: int = None) -> uuid.UUID:
        
        topics = self.get_topics(message_types)
        live_subscription_ids = []

        if start_millis and end_millis:
            data = await self.hist_client.get_range(topics, start_millis, end_millis)
            sorted_data = sorted(data, key=lambda x: x.timestamp_millis)
            for message in sorted_data:
                user_callback(message)
        
        else:
            for topic in topics:
                sub_id = await self.live_client.subscribe(topic, user_callback)
                live_subscription_ids.append(sub_id)

        master_sub_id = uuid.uuid4()
        self.subscriptions[master_sub_id] = live_subscription_ids
        return master_sub_id

    async def unsubscribe(self, master_subscription_id: uuid.UUID) -> bool:
        if master_subscription_id in self.subscriptions:
            live_sub_ids = self.subscriptions[master_subscription_id]
            results = []
            for sub_id in live_sub_ids:
                result = await self.live_client.unsubscribe(sub_id)
                results.append(result)
            del self.subscriptions[master_subscription_id]
            return all(results)  # Return True if all unsubscriptions were successful
        return False
