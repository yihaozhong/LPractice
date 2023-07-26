def count_balanced_strings(n, d):
    MOD = 10**9 + 7
    dp = [1]*26
    for _ in range(n-1):
        dp_new = [0]*26
        for j in range(26):
            for k in range(max(0, j-d), min(26, j+d+1)):
                dp_new[j] = (dp_new[j] + dp[k]) % MOD
        dp = dp_new
    return sum(dp) % MOD

def count_balanced_strings(n, d):
    MOD = 10**9 + 7
    dp = [1]*26
    for _ in range(n-1):
        dp_new = [0]*26
        for j in range(26):
            for k in range(max(0, j-d), min(26, j+d+1)):
                dp_new[j] = (dp_new[j] + dp[k]) % MOD
        dp = dp_new
    return sum(dp) % MOD


print(count_balanced_strings(2, 1))  # Expected output: 52
print(count_balanced_strings(3, 1))  # Expected output: 78
print(count_balanced_strings(4, 1))  # Expected output: 104
print(count_balanced_strings(2, 2))  # Expected output: 78
