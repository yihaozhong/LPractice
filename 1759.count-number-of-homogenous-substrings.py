#
# @lc app=leetcode id=1759 lang=python3
#
# [1759] Count Number of Homogenous Substrings
#

# @lc code=start

class Solution:
    def countHomogenous(self, s: str) -> int:
        count, total = 1, 1
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                count = 1
            else:
                count += 1
            total += count
        return total%(10**9 + 7)

# @lc code=end

