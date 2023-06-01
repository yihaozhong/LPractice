#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # nums.sort()
        # res = []
        # for i in range(len(nums)): # pivot
        #     if (nums[i-1] != nums[i]) or i == 0:
        #         lo, hi = i+1, len(nums) - 1
        #         while(lo < hi):
                    
        #             mySum = nums[lo] + nums[hi] + nums[i]
        #             # if (nums[hi] == nums[i]) or (nums[hi] == nums[lo]) or (nums[lo] == nums[i]):
        #             #     break
        #             if mySum < 0:
        #                 lo += 1
        #             elif mySum > 0:
        #                 hi -= 1
        #             else:
        #                 res.append([nums[lo] , nums[hi] , nums[i]])
        #                 lo += 1
        #                 hi -= 1
        #                 while lo < hi and nums[lo] == nums[lo - 1]:
        #                     lo += 1
        # return res

        # O(N^2) since two sum is O(n) and we call it n times
        # O(logn) to O(n) depend on the sorting algo

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


        # sol 3, no sorting needed, need to deal with dups if there are 1000+ 0
       
  
        res, dups = set(), set()
        seen = {}
        for i, val1 in enumerate(nums):
            if val1 not in dups:
                dups.add(val1)
                for j, val2 in enumerate(nums[i+1:]):
                    complement = -val1 - val2
                    if complement in seen and seen[complement] == i:
                        res.add(tuple(sorted((val1, val2, complement))))
                    seen[val2] = i
        return res
        # O(N^2) same reason above
        # O(n) for hashset
# @lc code=end

