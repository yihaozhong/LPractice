#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left <= right:
            mid = (left + right)//2

            if mid*mid <= x:
                ans = mid
                left = mid + 1
            else:
                right = mid -1
        return ans
    
    """
    This is the same as above

    def mySqrt(x: int) -> int:
        left, right = 0, x
        while left < right:
            mid = left + (right - left) // 2
            if mid * mid <= x:
                left = mid + 1
            else:
                right = mid
        return left - 1
    """
# @lc code=end

