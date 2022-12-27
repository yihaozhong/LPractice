#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = fast = 0
        while(fast < len(nums)):
            if (nums[fast] != val):
                # add ele to array
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        return slow

    # time: O(n)
        
# @lc code=end

