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