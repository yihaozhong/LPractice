#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        def twoSumClosest(start, nums, target):
            closest = float("inf")
            left, right = start, len(nums) - 1
            while(left < right):
                if abs(closest) > abs(target - (nums[left] + nums[right])):
                    closest = target - (nums[left] + nums[right])
                if (nums[left] + nums[right]) < target:
                    left += 1
                else:
                    right -= 1
            return target - closest
        
        delta = float("inf")
        nums.sort()
        # 固定 nums[i] 为三数之和中的第一个数，
        # 然后对 nums[i+1..] 搜索接近 target - nums[i] 的两数之和
        for i in range(len(nums)- 2):
            sum= twoSumClosest(i+1, nums, target - nums[i])+nums[i]
            if abs(delta) > abs(target - sum):
                delta = target - sum
        return target - delta      
# @lc code=end

