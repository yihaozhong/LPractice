#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # dict = {}
        # for i, ele in enumerate(nums):
        #     comp_ele = target - ele
        #     if comp_ele in dict:
        #         return [dict[comp_ele], i]
        #     else:
        #         dict[ele] = i

        dict = {}
        for i, ele in enumerate(nums):
            comp_ele = target - ele
            if comp_ele in dict:
                return [dict[comp_ele], i]
            else:
                dict[ele] = i 

    
        
# @lc code=end

