#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # def left_bound(nums, target):
        #     left = 0
        #     right = len(nums) -1
        #     while (left <= right):
        #         mid = (left + right)//2
        #         if (nums[mid] == target):
        #             right = mid -1
        #         elif (nums[mid] < target):
        #             left = mid + 1
        #         elif (nums[mid] > target):
        #             right = mid - 1
        #     if (left >= len(nums) or nums[left]!= target):
        #         return -1
        #     return left # left == right here

        # def right_bound(nums, target):
        #     left = 0
        #     right = len(nums) -1
        #     while (left <= right):
        #         mid = (left + right)//2
        #         if (nums[mid] == target):
        #             left = mid +1
        #         elif (nums[mid] < target):
        #             left = mid + 1
        #         elif (nums[mid] > target):
        #             right = mid - 1
        #     if (right < 0 or nums[right]!= target):
        #         return -1
        #     return right # left == right here

        # return [left_bound(nums, target), right_bound(nums, target)]

        def left_bound(nums, target):
            left, right = 0, len(nums) - 1
            left_index = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    left_index = mid 
                    right = mid- 1
                elif nums[mid] > target:
                    right = mid- 1
                else:
                    left = mid + 1
            return left_index
        
        def right_bound(nums, target):
            left, right = 0, len(nums) - 1
            right_index = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                    if nums[mid] == target:
                        right_index = mid
                else:
                    right = mid - 1
            return right_index
        return [left_bound(nums, target), right_bound(nums, target)]

# @lc code=end

