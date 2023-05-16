#
# @lc app=leetcode id=410 lang=python3
#
# [410] Split Array Largest Sum
#

# @lc code=start
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def feasible(sum):
            total = 0
            k_max = 1
            for n in nums:
                total += n
                if total > sum:
                    total = n
                    k_max += 1
            return k_max <= k
        
        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left  + right) //2

            if feasible(mid):
                right =  mid
            else:
                left = mid + 1

        return left
    
    # after exiting the while loop, left is the minimal k​ satisfying the condition function;
# @lc code=end

