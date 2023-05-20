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
    
    # sol 2

    # def removeDuplicates(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
        
    #     # Initialize the counter and the second pointer.
    #     j, count = 1, 1
        
    #     # Start from the second element of the array and process
    #     # elements one by one.
    #     for i in range(1, len(nums)):
            
    #         # If the current element is a duplicate, 
    #         # increment the count.
    #         if nums[i] == nums[i - 1]:
    #             count += 1
    #         else:
    #             # Reset the count since we encountered a different element
    #             # than the previous one
    #             count = 1
            
    #         # For a count <= 2, we copy the element over thus
    #         # overwriting the element at index "j" in the array
    #         if count <= 2:
    #             nums[j] = nums[i]
    #             j += 1
                
    #     return j
# @lc code=end

