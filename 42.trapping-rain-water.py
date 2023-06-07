#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start

# 不要考虑如何处理整个字符串，而是去思考应该如何处理每一个字符。


class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        l_max, r_max  = 0, 0
        result = 0
        while left < right:
            l_max = max(l_max, height[left])
            r_max = max(r_max, height[right])

            if l_max < r_max:
                result += (l_max - height[left])
                left += 1
            else:
                result += (r_max - height[right])
                right -= 1

        return result
# @lc code=end

