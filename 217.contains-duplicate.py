#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=startf

from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # myCounter = Counter(nums)
        # # print(myCounter)
        # return len(nums) != len(myCounter)

        dict = {}
        for i in nums:
            if i in dict:
                dict[i] +=1
            else:
                dict[i] = 1
        return len(nums) != len(dict)   
    
# @lc code=end

