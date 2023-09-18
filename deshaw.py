def solution(queries, min_length):
    trees = set()
    segments = {}
    res = []
    counter = 0

    for q in queries:
        left_neighbor = q - 1
        right_neighbor = q + 1
        left_end = q
        right_end = q
        
        # Merge two segments
        if left_neighbor in trees and right_neighbor in trees:
            left_end = segments[left_neighbor]
            right_end = segments[right_neighbor]
            del segments[left_neighbor]
            del segments[right_neighbor]
            
            # Update counter
            if right_neighbor - left_neighbor - 1 >= min_length:
                counter -= 1
            if left_neighbor - left_end + 1 >= min_length:
                counter -= 1
            if right_end - right_neighbor + 1 >= min_length:
                counter -= 1
            if right_end - left_end + 1 >= min_length:
                counter += 1
        
        # Extend segment to the left
        elif left_neighbor in trees:
            left_end = segments[left_neighbor]
            del segments[left_neighbor]
            
            # Update counter
            if left_neighbor - left_end + 1 >= min_length:
                counter -= 1
            if q - left_end + 1 >= min_length:
                counter += 1
        
        # Extend segment to the right
        elif right_neighbor in trees:
            right_end = segments[right_neighbor]
            del segments[right_neighbor]
            
            # Update counter
            if right_end - right_neighbor + 1 >= min_length:
                counter -= 1
            if right_end - q + 1 >= min_length:
                counter += 1
        
        # New segment
        else:
            if right_end - left_end + 1 >= min_length:
                counter += 1

        segments[left_end] = right_end
        segments[right_end] = left_end
        trees.add(q)
        res.append(counter)

    return res

# Test
queries = [2, 1, 3, 5, 6]
min_length = 2
print(solution(queries, min_length))
