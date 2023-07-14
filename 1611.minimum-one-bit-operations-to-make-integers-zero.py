#
# @lc app=leetcode id=1611 lang=python3
#
# [1611] Minimum One Bit Operations to Make Integers Zero
#

# @lc code=start
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        bin_str = bin(n)[2:]
        digit_count = len(bin_str)
        accumulator = 0
        sign = 1

        for i in range(digit_count):
            digit = int(bin_str[i])
            power = pow(2, digit_count - (i + 1)) if digit > 0 else 0
            steps = digit * (power * 2 - 1)

            accumulator += steps * sign
            sign = sign * (1 if digit == 0 else -1)

        return accumulator
# @lc code=end

