from collections import Counter
'''
def maxDistinctAfterSwaps(a, b, k):
    # Count occurrences of elements in both lists
    a_counts = Counter(a)
    b_counts = Counter(b)
    
    # Distinct elements in a and b
    distinct_a = set(a)
    distinct_b = set(b)
    
    # Elements in b but not in a
    diff = distinct_b - distinct_a
    
    # If there are no unique elements in b that are not in a, or no operations left
    if not diff or k == 0:
        return len(distinct_a)
    
    # For each element in the difference, swap it with the most frequent element in a
    # which is not in the target set 'diff'
    for elem in diff:
        if k == 0:
            break

        # Identify elements in a that are not in 'diff'
        possible_swap_elements = set(a_counts.keys()) - diff
        
        # Find the most frequent among the possible swap elements
        swap_element = max(possible_swap_elements, key=a_counts.get)
        
        # Swap operation: Reduce the count of the chosen element in a, and add the new element
        a_counts[swap_element] -= 1
        if a_counts[swap_element] == 0:
            del a_counts[swap_element]
        a_counts[elem] = a_counts.get(elem, 0) + 1
        
        k -= 1
    
    # The result is the number of keys in the updated a_counts
    return len(a_counts)
'''
import heapq

def maxDistinctAfterSwaps(a, b, k):
    # Count occurrences of elements in both lists
    a_counts = Counter(a)
    b_counts = Counter(b)
    
    # Distinct elements in a and b
    distinct_a = set(a)
    distinct_b = set(b)
    
    # Elements in b but not in a
    diff = distinct_b - distinct_a
    
    # If there are no unique elements in b that are not in a, or no operations left
    if not diff or k == 0:
        return len(distinct_a)
    
    # Initialize a max heap with elements of a that are not in 'diff'
    # We negate the counts to simulate a max heap as Python provides a min heap implementation
    heap = [-a_counts[elem] for elem in a_counts if elem not in diff]
    heapq.heapify(heap)
    
    # For each element in the difference, swap it with the most frequent element in a
    # which is not in the target set 'diff'
    for elem in diff:
        if k == 0 or not heap:
            break

        # Fetch the most frequent element count from the heap
        swap_count = -heapq.heappop(heap)
        
        # Identify the element associated with the count
        swap_element = [key for key, val in a_counts.items() if val == swap_count and key not in diff][0]
        
        # Swap operation: Reduce the count of the chosen element in a, and add the new element
        a_counts[swap_element] -= 1
        if a_counts[swap_element] == 0:
            del a_counts[swap_element]
        else:
            # If the element is still present in a, push it back to the heap with updated count
            heapq.heappush(heap, -a_counts[swap_element])
            
        a_counts[elem] = a_counts.get(elem, 0) + 1
        
        k -= 1
    
    # The result is the number of keys in the updated a_counts
    return len(a_counts)
# Test with the given example


‘’‘
def maxDistinctAfterSwaps(a, b, k):
    a_counts = Counter(a)
    b_counts = Counter(b)
    
    # Step 1: Calculate distinct elements
    distinct_a = set(a)
    distinct_b = set(b)
    
    # Step 2: Calculate potential gain
    potential_gain = distinct_b - distinct_a
    
    # Step 3: Sort 'a' by frequency
    a_sorted_by_freq = sorted(a_counts.keys(), key=lambda x: -a_counts[x])
    
    # Step 4: Perform swaps
    swaps = 0
    for candidate in potential_gain:
        if k <= 0:
            break
        if a_sorted_by_freq:
            most_frequent_a = a_sorted_by_freq.pop(0)
            while a_counts[most_frequent_a] <= 1 and a_sorted_by_freq:
                most_frequent_a = a_sorted_by_freq.pop(0)
            if a_counts[most_frequent_a] > 1:
                a_counts[most_frequent_a] -= 1
                swaps += 1
                k -= 1
    
    return len(distinct_a) + swaps


’‘’
a = [2,3,3,2,2]
b = [1,3,2,4,1]
k = 2
print(maxDistinctAfterSwaps(a, b, k))

print(maxDistinctAfterSwaps([1,1,4,5,5], [4,4,3,1,5], 2))
print(maxDistinctAfterSwaps([1,2,3], [4,5,6], 5))
