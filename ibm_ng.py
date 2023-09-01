from collections import deque

def allocate_ports(numberOfPorts, transmissionTime, packetIds):
    port_queues = [deque() for _ in range(numberOfPorts)]
    port_times = [0] * numberOfPorts

    res = []

    for time, packet in enumerate(packetIds, 1):
        cur_p = packet % numberOfPorts
        allocated = False
        
        for _ in range(numberOfPorts):
            if time >= port_times[cur_p]:
                port_queues[cur_p].append(packet)
                port_times[cur_p] = time + transmissionTime
                res.append(cur_p)
                allocated = True
                break
            else:
                cur_p = (cur_p + 1) % numberOfPorts


        if not allocated:
            cur_p = 0
            port_queues[cur_p].append(packet)
            port_times[cur_p] = time + transmissionTime
            res.append(cur_p)

    return res


def solution(moves):
    x, y = 0, 0
    visited = {(x, y)}
    for move in moves:
        if move == "^":
            y += 1
        elif move == "v":
            y -= 1
        elif move == "<":
            x -= 1
        elif move == ">":
            x += 1
        visited.add((x, y))
    
    if len(visited) != 5:
        return False
    

    visited.remove((0, 0))

    points = list(visited)
    distances = []
    for i in range(4):
        for j in range(i+1, 4):
            d = (points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2
            distances.append(d)

    unique_distances = set(distances)
    if len(unique_distances) != 2:
        return False
    if distances.count(min(unique_distances)) != 4 or distances.count(max(unique_distances)) != 2:
        return False
    
    return True

def eliminate_drivers_v4(lap_times):

    drivers = {entry.split()[0]: [int(entry.split()[1])] for entry in lap_times[0]}
    
    eliminated_order = []
    
    for lap in lap_times[1:]:
        for entry in lap:
            driver = entry.split()[0]
            time = int(entry.split()[1])
            if driver in drivers:  
                drivers[driver].append(time)
        

        current_lap = min([len(times) for times in drivers.values()]) - 1

        slowest_time = max([times[current_lap] for times in drivers.values()])
        
        to_eliminate = [driver for driver, times in drivers.items() if times[current_lap] == slowest_time]
        to_eliminate.sort() 
        

        eliminated_order.extend(to_eliminate)
        
   
        for driver in to_eliminate:
            del drivers[driver]

    remaining_drivers = list(drivers.keys())
    remaining_drivers.sort()
    eliminated_order.extend(remaining_drivers)

    return eliminated_order
# Sample test
lap_times_v3 = [["A", "150", "B", "155", "C", "160"],
                ["A", "155", "B", "150"],
                ["A", "160", "B", "155"]]
eliminate_drivers_v3(lap_times_v3)


def optimized_min_separated_difference(numbers, separation):
    sorted_numbers = sorted(enumerate(numbers), key=lambda x: x[1])

    min_diff = float('inf')
    for i in range(1, len(sorted_numbers)):
        if abs(sorted_numbers[i][0] - sorted_numbers[i-1][0]) >= separation:
            diff = abs(sorted_numbers[i][1] - sorted_numbers[i-1][1])
            min_diff = min(min_diff, diff)

    if min_diff == float('inf'):
        return None
            
    return min_diff

print(optimized_min_separated_difference([3, 3, 3, 6, 6, 6, 9, 9, 9], 3))

def final_min_separated_difference(numbers, separation):

    sorted_numbers = sorted(enumerate(numbers), key=lambda x: x[1])

    min_diff = float('inf')

    for i in range(len(sorted_numbers)):
        j = i + 1
        while j < len(sorted_numbers) and sorted_numbers[j][0] - sorted_numbers[i][0] < separation:
            j += 1
        
        while j < len(sorted_numbers) and sorted_numbers[j][1] - sorted_numbers[i][1] < min_diff:
            diff = abs(sorted_numbers[j][1] - sorted_numbers[i][1])
            min_diff = min(min_diff, diff)
            j += 1

    if min_diff == float('inf'):
        return None

    return min_diff
