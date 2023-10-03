# Initialize the prefix array
max_val = 10**6  
prefix = [0] * (max_val + 1)

def has_unique_digits(n):
    digits = set()
    for digit in str(n):
        if digit in digits:
            return False
        digits.add(digit)
    return True

for i in range(1, max_val + 1):
    prefix[i] = prefix[i - 1] + has_unique_digits(i)


def query_with_prefix(L, R):
    return prefix[R] - prefix[L - 1] if L > 0 else prefix[R]


