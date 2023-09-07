import heapq

def earlies(graph, start, end, current_time):
    pq = [(current_time, start)]

    earliest_ime = {node: float('inf') for node in graph}
    earliest_ime[start] = current_time

    while pq:
        time, node = heapq.heappop(pq)

        if node == end:
            return time
        
        for neighbor, schedules in graph[node]:
            for st_time, end_time in schedules:
                if time <= st_time:
                    arrival = st_time
                elif time <= end_time:
                    arrival = time
                else:
                    continue
                
                if arrival < earliest_ime[neighbor]:
                    earliest_ime[neighbor] = arrival
                    heapq.heappop(pq, (arrival, neighbor))

    return -1