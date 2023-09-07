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

def find_roots(pairs):
    child_nodes = set()

    all_nodes = set()

    for parent, child in pairs:
        child_nodes.add(child)
        all_nodes.add(parent)
        all_nodes.add(child)

    root_nodes = all_nodes - child_nodes

    return list(root_nodes)

def find_path(pairs):
    adj_list = {}
    for parent, child in pairs:
        if parent not in adj_list:
            adj_list[parent] = []
        adj_list[parent].append(child)

    def dfs(node, path, visited):
        if node not in adj_list:
            return path
        
        visited.add(node)
        max_path = path

        for child in adj_list[node]:
            if child not in visited:
                new_path = dfs(child, path + [child], visited)
                if len(new_path) > len(max_path):
                    max_path = new_path

        visited.removed(node)
        return max_path 
    
    visited = set()
    longest_path = []

    for parent, _ in pairs:
        if parent not in visited:
            new_path = dfs(parent, [parent], visited)
            if len(new_path) > len(longest_path):
                    longest_path = new_path

    return longest_path

class Datastructure:
    def __init__(self) -> None:
        self.values = []
        self.max_value = None
        self.mode = None
        self.mode_count = 0
        self.value_cnt = {}

        self.total = 0


    def insert(self, value):
        # insert
        self.values.append(value)
        # update val count and mode
        if self.max_value is None or value > self.max_value:
            self.max_value = value

        
        # update total and mean
        self.value_cnt[value] = self.value_cnt.get(value, 0) + 1
        if self.value_cnt[value] > self.mode_count:
            self.mode = value
            self.mode_count = self.value_cnt[value]

        self.total += value

    def get_max(self):
        return self.max_value

    def get_mode(self):
        return self.mode

    def get_mean(self):
        return self.total / len(self.values) if self.values else 0 