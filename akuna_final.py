import math
from collections import defaultdict


def calEquation(self, equations, values, queries):
    graph = defaultdict(defaultdict)

    # construct the graph
    for (dividend, divisor), val in zip(equations, values):
        graph[dividend][divisor] = val
        graph[divisor][dividend] = 1/val

    def dfs(start, target, product, visited=None):
        if visited is None:
            visited = set()

        visited.add(start)
        neighbor = graph[start]
        acc = - 1.0

        if target in neighbor:
            acc = product * neighbor[target]
        else:
            for i, val in neighbor.items():
                if i in visited:
                    continue
                acc = dfs(i, target, product * val, visited)
                if acc != -1.0:
                    break
        visited.remove(start)
        return acc

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


def dfs_abt(rates):
    def dfs(node, target, graph, visited, rate, curr_path, path_and_profit):
        # reach to start, cycle
        if node == target and visited[node]:
            # return rate if rate > 1 else None
            if rate > path_and_profit[0]:
                path_and_profit[0] = rate
                path_and_profit[1] = curr_path + [target]
            return None

        if visited[node]:
            return None

        # a b 2; b c 0.5; c a 0.4
        visited[node] = True
        # max_rate = 0
        curr_path.append(node)

        for neighbor, exchange_rate in graph[node]:
            dfs(neighbor, target, graph, visited, rate *
                exchange_rate, curr_path, path_and_profit)

        visited[node] = False
        # return max_rate if max_rate > 1 else None
        curr_path.pop()

    graph = {}
    for src, dest, rate in rates:
        if src not in graph:
            graph[src] = []
        graph[src].append((dest, rate))

    path_and_profit = [0, []]

    for currency in graph:
        visited = {node: False for node in graph}
        dfs(currency, currency, graph, visited, 1, [], path_and_profit)

    return path_and_profit


rates = [
    ['USD', 'EUR', 0.8],
    ['USD', 'JPY', 105],
    ['EUR', 'JPY', 130],
    ['EUR', 'GBP', 0.9],
    ['GBP', 'CHF', 1.2],
    ['CHF', 'JPY', 115],
    ['CHF', 'USD', 0.95],
    ['JPY', 'INR', 0.7],
    ['INR', 'USD', 0.014],
    ['INR', 'EUR', 0.011],
    ['GBP', 'USD', 1.3]
]
print(dfs_abt(rates))


# a*b*c > 1 profitable
# log(a*b*b) = loga + logb + logc > log1 = 0 profitable
# loga + logb + logc > 0 profitable (maximal total weight)

# finding the shortest path, minimal total weight
# -loga - logb - logc < 0 profitable (take -log)

# a negative cycle means profitable arbitrage

# O(N*(N+E)), worst case, Edge = N*2, O(N*3)
# O(N*E),

# finding negative weight cycle / positive weight cycle

# longest path is the most profitable one (positive log)
# Negate all the weights of the edges and use Bellman Ford. Please note that,
# Bellman-Ford algorithm works for negative edge weight unlike Dijkstra.
# shortest path is the most profitable one (negative log transformation)
# bellman ford


def bellman_ford_arb(rates):
    # O(E)
    g = defaultdict(list)
    currencies = set()
    for src, dest, rate in rates:
        g[src].append((dest, -math.log(float(rate))))
        currencies.add(src)
        currencies.add(dest)


    # O(V*E)
    def bellman_ford(graph, src):
        distances = {currency: float("inf") for currency in currencies}
        distances[src] = 0
        previous = {node: None for node in graph}
        # V-1 times, each we iter ove all N nodes
        for _ in range(len(currencies) - 1):
            for node in graph:  # tuple
                for neighbor, rate in graph[node]:
                    # relaxation equation, dp thinking
                    if distances[node] + rate < distances[neighbor]:
                        distances[neighbor] = distances[node] + rate
                        previous[neighbor] = node

        # check for negative weight cycle
            # iterate one more times, check if we get shorter path by including one more edge
        # o(v+e)
        for node in graph:
            for neighbor, rate in graph[node]:
                if distances[node] + rate < distances[neighbor]:
                    # return True

                    # track back the cycle
                    cycle = [neighbor, node]
                    while previous[node] not in cycle:
                        cycle.append(previous[node])
                        node = previous[node]
                    cycle.append(previous[node])
                    cycle = cycle[cycle.index(previous[node]):]
                    cycle = cycle[::-1]

                    print(cycle)
                    # compute the profit
                    profit = 0
                    for i in range(len(cycle) - 1):
                        for neighbor, weight in graph[cycle[i]]:
                            if neighbor == cycle[i+1]:
                                profit += weight
                                break

                    return math.exp(-profit), cycle
        return 0, []

    # max_profit = 0
    # max_path = None
    # for src in currencies:
    #     profit, cycle = bellman_ford(g, src)
    #     if profit >= max_profit:
    #         max_profit = profit
    #         max_path = cycle.copy()
    # return max_profit, max_path

    # or 
    profit, cycle = bellman_ford(g, next(iter(g)))
    return profit, cycle

print(bellman_ford_arb([['USD', 'JPY', '20'], ['JPY', 'INR', '22'], ['INR', 'USD', '0.025']]))
print(bellman_ford_arb(rates))
def dfs_arb_any(rates):
    def dfs(node, target, graph, visited, stack, rate, curr_path):
        # If the node matches the target and we've visited the node before, we have a cycle
        if node == target and node in stack:
            if rate > 1:
                return rate, curr_path + [target]
            return None, []

        if node in visited:
            return None, []

        visited.add(node)
        stack.add(node)
        curr_path.append(node)

        for neighbor, exchange_rate in graph[node]:
            profit, cycle = dfs(neighbor, target, graph, visited, stack, rate * exchange_rate, curr_path)
            if cycle:  # If we find a cycle, return immediately
                return profit, cycle

        stack.remove(node)
        curr_path.pop()
        return None, []

    graph = defaultdict(list)
    for src, dest, rate in rates:
        graph[src].append((dest, rate))

    for currency in graph:
        visited = set()
        stack = set()
        profit, cycle = dfs(currency, currency, graph, visited, stack, 1, [])
        if cycle:  # Return the first found cycle
            return profit, cycle

    return None, []

print(dfs_arb_any(rates))
            
            
