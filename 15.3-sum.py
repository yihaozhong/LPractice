#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = []
        for i in range(len(nums)): # pivot
            if (nums[i-1] != nums[i]) or i == 0:
                lo, hi = i+1, len(nums) - 1
                while(lo < hi):
                    
                    mySum = nums[lo] + nums[hi] + nums[i]
                    # if (nums[hi] == nums[i]) or (nums[hi] == nums[lo]) or (nums[lo] == nums[i]):
                    #     break
                    if mySum < 0:
                        lo += 1
                    elif mySum > 0:
                        hi -= 1
                    else:
                        res.append([nums[lo] , nums[hi] , nums[i]])
                        lo += 1
                        hi -= 1
                        while lo < hi and nums[lo] == nums[lo - 1]:
                            lo += 1
        return res


# @lc code=end

