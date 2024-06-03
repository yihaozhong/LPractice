# 回溯算法是在遍历「树枝」DFS 算法是在遍历「节点」 

# 抽象地说，解决一个回溯问题，实际上就是遍历一棵决策树的过程，树的每个叶子节点存放着一个合法答案。
# 你把整棵树遍历一遍，
# 把叶子节点上的答案都收集起来，就能得到所有的合法答案。

'''
站在回溯树的一个节点上，你只需要思考 3 个问题：

1、路径：也就是已经做出的选择。

2、选择列表：也就是你当前可以做的选择。

3、结束条件：也就是到达决策树底层，无法再做选择的条件。

'''

# permutations, combinations, subsets
# a more specialized form of DFS 
# finding all possible solutions to a problem by exploring all potential paths 
def backtrack(solution, path, choices):
    # Check if we've reached the end condition
    if end_condition(path):
        # If so, add the current path to the solution
        solution.append(list(path))
        return
    
    # Iterate through all possible choices
    for choice in choices:
        if choice not in path: choice # avoid cycle
            # Make a choice
            path.append(choice)
            # Explore further with the current choice added to the path
            backtrack(solution, path, update_choices(choices, choice))
            # Undo the choice (backtrack)
            path.pop()
        

def solve():
    solution = []
    path = []
    choices = initial_choices()  # Define the initial choices
    backtrack(solution, path, choices)
    return solution


# pathfinding, detecting cycles in a graph
# The primary goal is to visit all nodes of a graph or tree.
# It traverses as far as possible along a branch before backtracking. 

def dfs(node, visited, graph):
    # Mark the node as visited
    visited.add(node)
    
    # Process the node (if needed)
    process(node)
    
    # Explore each adjacent node
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, visited, graph)

def solve(graph):
    visited = set()
    for node in graph:
        if node not in visited:
            dfs(node, visited, graph)
            
            
'''
DFS (has_path):

Searches for a single path.
Stops once the target is found.
Marks nodes as visited to avoid cycles.
Returns a boolean indicating the presence of a path.


Backtracking (all_paths):

Searches for all possible paths.
Continues exploring even after finding a path.
Uses the current path to avoid cycles.
Returns a list of all paths.


'''