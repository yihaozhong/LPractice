from collections import defaultdict

# Function to create an adjacency list representation of the graph
def create_graph(da, ia):
    graph = defaultdict(list)

    # Add all tasks to the graph
    for task in set(da + ia):
        graph[task]


    # Add dependencies
    for d, i in zip(da, ia):
        graph[d].append(i)

    return graph
def dfs(graph, node, visited, rec_stack):
    visited.add(node)
    rec_stack.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            if dfs(graph, neighbor, visited, rec_stack):
                return True
        elif neighbor in rec_stack:
            return True

    rec_stack.remove(node)
    return False

def find_cycles(graph):
    visited = set()
    rec_stack = set()

    for node in graph:
        if node not in visited:
            if dfs(graph, node, visited, rec_stack):
                return True
    return False


def count_performable_tasks(da, ia):
    # Create the graph
    graph = create_graph(da, ia)

    # Find cycles
    cycles = find_cycles(graph)

    # Return the number of tasks that can be performed
    return len(da) - cycles

# Testing the function with the example provided
da = [1, 2, 3, 4, 6, 5] # [1, 2, 3, 4, 5]
ia = [7, 6, 4, 1, 2, 1] # [4, 5, 1, 3, 2]
print(count_performable_tasks(da, ia))
