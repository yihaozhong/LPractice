#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_window, ans = 0, float('inf')

        left = 0
        for right in range(len(nums)):
            min_window += nums[right]
            while min_window >= target:
                ans = min(ans, right - left + 1)
                min_window -= nums[left]
                left += 1
        if ans == float('inf'):
            return 0

        return ans
        
# @lc code=end

