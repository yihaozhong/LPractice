#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        # sign = True
        result = 0
        # if x < 0:
        #     sign = True
        #     x *= -1
        # else:
        #     sign = False
        sign = -1 if x < 0 else 1
        x *= sign  # Make x positive for ease of processing
        
        # for i, digit in enumerate(str(x)): # int is not iterable
        #     if digit == '0' and i == len(str(x)):
        #         return result*-1 if sign else result
        #     else:
        #         result += 10**i * int(digit)
        
        while x!= 0:
            digit = x % 10
            x //= 10
            result = result * 10 + digit
            
        if result > (2**31 - 1):
            return 0
        return result*sign
    
# poping digit
# pop = x % 10
# x /= 10
# @lc code=end

