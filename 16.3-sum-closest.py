#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        def twoSumClosest(i, nums, target):
            left, right = i, len(nums) - 1
            delta = float('inf')
            while left < right:
                sum_ = nums[left] + nums[right]
                if abs(delta) > abs(target - sum_):
                    delta = target - sum_
                if sum_ < target:
                    left += 1
                else:
                    right -= 1
            return target - delta
        
        
        delta = float("inf")
        nums.sort()
        # 固定 nums[i] 为三数之和中的第一个数，
        # 然后对 nums[i+1..] 搜索接近 target - nums[i] 的两数之和
        for i in range(len(nums)- 2):
            sum_ = twoSumClosest(i+1, nums, target - nums[i])+nums[i]
            if abs(delta) > abs(target - sum_):
                delta = target - sum_
        return target - delta      
# @lc code=end

