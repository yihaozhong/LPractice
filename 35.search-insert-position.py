#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right - left)//2
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                right = mid-1
            else:
                left = mid + 1
        return left # return mid give error
        """
        
        ans = 0
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) //2
            if target < nums[mid]:
                right = mid - 1

            else:
                if target == nums[mid]:
                    ans = mid
                    left = mid + 1
                else:
                    left = mid + 1
                    ans = left
        return ans
# @lc code=end

