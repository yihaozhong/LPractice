#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # remove the zero
        slow = fast = 0
        while (fast < len(nums)):
            if (nums[fast] != 0):
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        # make all the rest to 0
        while (slow < len(nums)):
            nums[slow] = 0
            slow += 1
        
        
# @lc code=end

