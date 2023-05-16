#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 0, n
        first_index = -1
        while left <= right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                first_index = mid
                right = mid - 1
            else:
                left = mid + 1
        return first_index
# @lc code=end

