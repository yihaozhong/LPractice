def to_fibonacci(x):
    # change x to a fibonacci number in minimum step
    # if x == 0:
    #     return 0
    # if x == 1:
    #     return 0
    # # Initialize fibonacci numbers
    # a, b = 0, 1
    # # Generate fibonacci numbers until we get a number >= x
    # while b < x:
    #     a, b = b, a + b

    # # Return the minimum difference between x and the nearest fibonacci numbers
    # return min(b - x, x - a)

    # use binary search
    fibonacci_numbers = [0, 1]
    a, b = 0, 1
    while b <= 1_000_000:
        a, b = b, a + b
        fibonacci_numbers.append(b)
    low, high = 0, len(fibonacci_numbers) - 1
    while low <= high:
        mid = (low + high) // 2
        if fibonacci_numbers[mid] == x:
            return x
        elif fibonacci_numbers[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    # Return the closest Fibonacci numbers (either side of x)
    if low == len(fibonacci_numbers):
        return fibonacci_numbers[high]
    elif high == -1:
        return fibonacci_numbers[low]
    else:
        return fibonacci_numbers[low] if (fibonacci_numbers[low] - x) < (x - fibonacci_numbers[high]) else fibonacci_numbers[high]


def max_apple(A):
    # return maximum apple that could fit in the box, A[0] is the capacility
    cap = 5000 - A[0]
    apples = A[1:]
    apples.sort()
    total, cnt = 0, 0

    for a in apples:
        if total + a <= cap:
            total += a
            cnt += 1
        else:
            break
    return cnt

def toHexspeak(s):

    # convert s to Hex, then 0 is o, 1 is l, hexspeak is that only has ABCDEFIO letters
    
    # Convert s to integer
    num = int(s)
    
    # Convert integer to hexadecimal and convert to uppercase
    hex_str = hex(num)[2:].upper()
    
    # Replace '0' with 'O' and '1' with 'L'
    hex_str = hex_str.replace('0', 'O').replace('1', 'L')
    
    # Check for valid Hexspeak characters
    for char in hex_str:
        if char not in "ABCDEFILO":
            return "ERROR"
    
    return hex_str

def final_score(arr):
    # if a student sit between 2 better score, this student score increase 1
    # if sit between 2 worse score, decrease 1
    # repeat until no student change score
    while True:
        # Create a new list of adjusted scores
        new_arr = arr.copy()
        
        for i in range(1, len(arr) - 1):  # Only adjust scores for students in between
            # Check if the student is sitting between two better scores
            if arr[i-1] > arr[i] and arr[i+1] > arr[i]:
                new_arr[i] += 1
            
            # Check if the student is sitting between two worse scores
            elif arr[i-1] < arr[i] and arr[i+1] < arr[i]:
                new_arr[i] -= 1
        
        # If no scores changed, break the loop
        if new_arr == arr:
            break
        
        # Update the original array
        arr = new_arr
        
    return arr