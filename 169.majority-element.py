#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result = dict()
        for i in nums:
            if i in result:
                result[i] += 1
            else:
                result[i] = 1
            if result[i] > len(nums)//2:
                    return i
        
# @lc code=end

