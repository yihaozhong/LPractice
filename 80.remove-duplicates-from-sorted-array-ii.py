#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 111 22 3
        slow, fast = 0, 0
        count = 0
        while fast < len(nums):
            if nums[slow] != nums[fast]:
                slow+=1
                nums[slow] = nums[fast]
                
            elif (slow < fast and count < 2):
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
            count += 1
            if fast <len(nums) and nums[fast] != nums[fast - 1]:
                count = 0
        return slow+1
# @lc code=end

