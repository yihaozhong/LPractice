#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
from typing import List
# @lc code=start

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        results = []
        for i, element in enumerate(nums):
            if i == 0 or (nums[i] != nums[i-1] and element <= 0):
                lo, hi = i + 1, len(nums) - 1
                while lo < hi:
                    sum3 = element + nums[lo] + nums[hi]
                    if sum3 > 0:
                        hi -= 1
                    elif sum3 < 0:
                        lo += 1
                    else:
                        results.append([element, nums[lo], nums[hi]])
                        hi -= 1
                        lo += 1
                        while lo < hi and nums[lo] == nums [lo - 1]:
                            lo += 1
                        
        return results
                
        # O(N^2) since two sum is O(n) and we call it n times
        # O(logn) to O(n) depend on the sorting algo
print(Solution().threeSum([-1,0,1,2,-1,-4]))
        # sol 2
    #     res = []
    #     nums.sort()
    #     for i in range(len(nums)):
    #         if nums[i] > 0:
    #             break
    #         if i == 0 or nums[i - 1] != nums[i]:
    #             self.twoSum(nums, i, res)
    #     return res

    # def twoSum(self, nums: List[int], i: int, res: List[List[int]]):
    #     seen = set()
    #     j = i + 1
    #     while j < len(nums):
    #         complement = -nums[i] - nums[j]
    #         if complement in seen:
    #             res.append([nums[i], nums[j], complement])
    #             while j + 1 < len(nums) and nums[j] == nums[j + 1]:
    #                 j += 1
    #         seen.add(nums[j])
    #         j += 1

    # O(N^2) same reason above
    # O(n) for hashset

        # nSum 系列问题的核心思路就是排序 + 双指针
        # sol 3, no sorting needed, need to deal with dups if there are 1000+ 0
       
  
        # res, dups = set(), set()
        # seen = {}
        # for i, val1 in enumerate(nums):
        #     if val1 not in dups:
        #         dups.add(val1)
        #         for j, val2 in enumerate(nums[i+1:]):
        #             complement = -val1 - val2
        #             if complement in seen and seen[complement] == i:
        #                 # ensure that the complement found is from a number in the array that comes after val1 and val2, thus avoiding using the same number twice. 
        #                 # Remember, the requirement is to find three different numbers that sum up to zero.
        #                 res.add(tuple(sorted((val1, val2, complement))))
        #             seen[val2] = i
        # return res
        # O(N^2) same reason above
        # O(n) for hashset

        # the algorithm is allowed to use the 2 at index 3 in nums twice: once for val2 and once for the complement
# @lc code=end

