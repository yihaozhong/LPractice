from collections import deque


def getResult(arrival, direction):
    n = len(arrival)
    # Queues for ascending and descending hikers
    asc_queue, desc_queue = deque(), deque()
    pass_times = [-1] * n  # List to store when each hiker passes
    last_passed = None  # Variable to track the direction of the last hiker that passed
    time = 0  # Current time

    while time <= max(arrival) or asc_queue or desc_queue:
        hiker_passed = False  # Flag to indicate if a hiker has passed in the current second

        # Enqueue any hikers that have arrived at this time
        for i, t in enumerate(arrival):
            if t == time:
                if direction[i] == 0:
                    asc_queue.append(i)
                else:
                    desc_queue.append(i)

        # Decide which hiker goes next based on rules
        if desc_queue and (last_passed is None or last_passed == 1) and not hiker_passed:
            hiker = desc_queue.popleft()
            pass_times[hiker] = time
            last_passed = 1
            hiker_passed = True
        elif asc_queue and not hiker_passed:
            hiker = asc_queue.popleft()
            pass_times[hiker] = time
            last_passed = 0
            hiker_passed = True

        # Increment the time if a hiker passed, otherwise skip to the next earliest arrival time
        if hiker_passed:
            time += 1
        else:
            # Skip to the next earliest arrival time
            potential_arrivals = [t for t in arrival if t > time]
            if potential_arrivals:
                time = min(potential_arrivals)
            else:
                time += 1

    return pass_times
