from collections import defaultdict

def count_infection_ways(n, infected_houses):
    # Initialize the adjacency list and the state of the houses
    adjacency_list = defaultdict(list)
    for i in range(1, n+1):
        if i > 1:
            adjacency_list[i].append(i-1)
        if i < n:
            adjacency_list[i].append(i+1)

    state = [0] * (n+1)
    for house in infected_houses:
        state[house] = 1

    # Define the DFS function
    def dfs(house):
        # If all houses are infected, increment the counter
        if sum(state) == n:
            nonlocal count
            count += 1
            return

        # Infect all uninfected neighbors
        # for neighbor in adjacency_list[house]:
        #     if state[neighbor] == 0:
        #         state[neighbor] = 1
        #         dfs(neighbor)
        #         state[neighbor] = 0


                # Infect all uninfected neighbors of each infected house
        for house in range(1, n+1):
            if state[house] == 1:
                for neighbor in adjacency_list[house]:
                    if state[neighbor] == 0:
                        state[neighbor] = 1
                        dfs()
                        state[neighbor] = 0

    # Call the DFS function for each infected house
    count = 0
    for house in infected_houses:
        dfs(house)

    # Return the counter
    return count

# Testing the function with the provided examples
print(count_infection_ways(5, [1, 5]))
print(count_infection_ways(6, [3, 5]))
