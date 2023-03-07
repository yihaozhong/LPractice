#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums.sort()

        longtest_con = 1
        current_con = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                if nums[i] == nums[i-1] + 1:
                    current_con += 1
                else:
                    longtest_con = max(longtest_con, current_con)
                    current_con = 1
        return max(longtest_con, current_con)
    
# @lc code=end

