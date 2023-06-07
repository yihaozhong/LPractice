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
    
    # 你如果移动较低的那一边，那条边可能会变高，使得矩形的高度变大，进而就「有可能」使得矩形的面积变大；相反，如果你去移动较高的那一边，
    # 矩形的高度是无论如何都不会变大的，所以不可能使矩形的面积变得更大。
    # same as max_area = max(max_Area, min(height[left]), height[right])*(right - left)
# @lc code=end

