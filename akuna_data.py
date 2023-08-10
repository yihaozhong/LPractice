import heapq


def max_knowledge_gain(D, S, E, A, K):
    events = []
    for s, e, a in zip(S, E, A):
        events.append((s, True, a))  # start of a meeting
        events.append((e+1, False, a))  # end of a meeting
    events.sort()

    max_gain = 0
    active_knowledges = []  # This is a max-heap
    knowledge_count = {}  # Keeps count of each knowledge value in the heap

    for _, is_start, knowledge in events:
        if is_start:
            heapq.heappush(active_knowledges, -knowledge)
            knowledge_count[knowledge] = knowledge_count.get(knowledge, 0) + 1
        else:
            if knowledge_count.get(knowledge, 0) > 0:
                knowledge_count[knowledge] -= 1
                if knowledge_count[knowledge] == 0:
                    active_knowledges.remove(-knowledge)
                    heapq.heapify(active_knowledges)

        # Calculate the maximum gain possible on the current day
        temp = []
        current_gain = 0
        for _ in range(min(K, len(active_knowledges))):
            val = -heapq.heappop(active_knowledges)
            current_gain += val
            temp.append(val)

        # Return the knowledge values to the max heap
        for val in temp:
            heapq.heappush(active_knowledges, -val)

        max_gain = max(max_gain, current_gain)

    return max_gain


# Example
D = 3
S = [1, 1, 2]
E = [2, 3, 3]
A = [10, 20, 30]
K = 2

print(max_knowledge_gain(D, S, E, A, K))  # Expected output: 50
