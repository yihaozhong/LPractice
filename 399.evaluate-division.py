#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#

# @lc code=start
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(defaultdict)
        
        # construct a graph
        for (dividend, divisor), val in zip(equations, values):
            # adding dividend and divisor as nodes
            graph[dividend][divisor] = val
            # the edge as value and the reversed edge as reversed edge
            graph[divisor][dividend] = 1/val

        # use a backtracking to traverse the graph

        def dfs(start, target, product, visited = None):
            if visited is None:
                visited = set()

            visited.add(start)
            neighbour = graph[start]
            acc = -1.0

            if target in neighbour:
                acc = product * neighbour[target]
            else:
                for i, val in neighbour.items():
                    if i in visited:
                        continue
                    acc = dfs(i, target, product * val, visited)
                    if acc != -1.0:
                        break
            visited.remove(start)
            return acc


        # for each queries, run through the graph to get the output
        output = []
        for dividend, divisor in queries:
            if dividend not in graph or divisor not in graph:
                acc = -1.0
            elif dividend == divisor:
                acc = 1.0
            else:
                acc = dfs(dividend, divisor, 1)
            output.append(acc)
        return output
# @lc code=end

