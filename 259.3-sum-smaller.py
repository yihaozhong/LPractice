#
# @lc app=leetcode id=259 lang=python3
#
# [259] 3Sum Smaller
#

# @lc code=start
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        def twoSumSmaller(nums, target, start):
            sum = 0
            left, right = start, len(nums) - 1
            while left < right:
                if nums[left] + nums[right] < target:
                    sum += right - left
                    left += 1
                else:
                    right -= 1
            return sum
        res = 0
        nums.sort()
        for i in range(len(nums)):
            res += twoSumSmaller(nums, target - nums[i], i+1)
        return res
    
    # this use two pointer, we can also use binary search
    # time complexity: O(n^ 2), two sum us O(n), threeSum use o(nlogn) to sort, 
    #   so O(nlogn + n^2) -> O(N^2)
# @lc code=end
