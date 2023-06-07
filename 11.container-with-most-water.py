#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            if height[left] <= height[right]:
                max_area = max(max_area, height[left]* (right - left))
                left += 1
            else:
                max_area = max(max_area, height[right]* (right - left))
                right -= 1

        return max_area
    
    # same as max_area = max(max_Area, min(height[left]), height[right])*(right - left)
# @lc code=end

