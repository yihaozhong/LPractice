#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def left_bound(nums, target):
            left = 0
            right = len(nums) -1
            while (left <= right):
                mid = (left + right)//2
                if (nums[mid] == target):
                    right = mid -1
                elif (nums[mid] < target):
                    left = mid + 1
                elif (nums[mid] > target):
                    right = mid - 1
            if (left >= len(nums) or nums[left]!= target):
                return -1
            return left # left == right here

        def right_bound(nums, target):
            left = 0
            right = len(nums) -1
            while (left <= right):
                mid = (left + right)//2
                if (nums[mid] == target):
                    left = mid +1
                elif (nums[mid] < target):
                    left = mid + 1
                elif (nums[mid] > target):
                    right = mid - 1
            if (right < 0 or nums[right]!= target):
                return -1
            return right # left == right here

        return [left_bound(nums, target), right_bound(nums, target)]
        
# @lc code=end

