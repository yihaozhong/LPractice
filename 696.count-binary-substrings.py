#
# @lc app=leetcode id=696 lang=python3
#
# [696] Count Binary Substrings
#

# @lc code=start
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # 0 0 1 1 0 0 1 1
        # group it in the result, result = [2, 2, 2, 2]
        result = []
        for i in s.replace('01', '0 1').replace('10', '1 0').split():
            result.append(len(i))
        for a, b in zip(result, result[1:]):
            print(a, b)
        return sum(min(a, b) for a, b in zip(result, result[1:]))
# @lc code=end

