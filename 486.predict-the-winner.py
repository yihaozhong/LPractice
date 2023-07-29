#
# @lc app=leetcode id=486 lang=python3
#
# [486] Predict the Winner
#

# @lc code=start
import collections
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = collections.defaultdict(int)
        def maxDiff(left,right):
            if (left, right) in memo:
                return memo[(left, right)]
            if left == right:
                return nums[left]
            score_left = nums[left] - maxDiff(left + 1, right)
            score_right = nums[right] - maxDiff(left, right - 1)
            memo[(left, right)] = max(score_left, score_right)
            return memo[(left, right)] 
        return maxDiff(0, n-1) >= 0
# @lc code=end

