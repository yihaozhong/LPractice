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


test_cases = [
    [4850, 100, 30, 30, 100, 50, 100],
    [5, 1, 1, 1, 1, 2, 2],
    [20, 10, 5, 5, 2, 2, 2]
]

results = [max_apple(case) for case in test_cases]
print(results)
