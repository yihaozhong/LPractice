import math
from typing import List
from collections import deque


def solve(n: int, infected_houses: List[int]):
    frontier_queue = deque()  # Initialize a frontier queue for BFS
    visit = set()  # A set to maintain visited (i.e. infected) houses

    # Mark the infected houses as visited. Also add them to the frontier queue.
    for infected_house in infected_houses:
        frontier_queue.append(infected_house)
        visit.add(infected_house)

    # Helper function to add the next house to the frontier.
    def add_house(_house: int):
        if _house < 1 or _house > n or _house in visit:
            return
        frontier_queue.append(_house)
        visit.add(_house)

    level = 0
    cnt = 0
    # Keep doing this while frontier queue is not empty.
    while frontier_queue:
        # Iterate over all the houses in the frontier before processing the next set of frontier.
        for infected_house in range(len(frontier_queue)):
            house = frontier_queue.popleft()
            visit.add(house)
            add_house(house - 1)
            add_house(house + 1)
        # Keep a track of how far the frontier is from the starting points.
        level += 1
        # Add the factorial of the current frontier to the total count.
        if level and len(frontier_queue) > 1:
            cnt += math.factorial(len(frontier_queue))
    return cnt


print(solve(6, [3, 5]))  # Ans = 6
print(solve(5, [1, 5]))  # Ans = 2


#### sol 2
def solve(n: int, infected_houses: List[int]):
    frontier_queue = deque()
    visit = set()

for infected_house in infected_houses:
    frontier_queue.append(infected_house)
    visit.add(infected_house)


def add_house(_house: int):
    if _house < 1 or _house > n or _house in visit:
        return
    frontier_queue.append(_house)
    visit.add(_house)

level = 0
cnt = 1
while frontier_queue:
    for infected_house in range(len(frontier_queue)):
        house = frontier_queue.popleft()
        visit.add(house)
        add_house(house - 1)
        add_house(house + 1)
    level += 1
    if level and len(frontier_queue) > 1:
        cnt *= math.factorial(len(frontier_queue))
return cnt

# set cnt = 1