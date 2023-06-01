#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # i, j = 0, 0
        # if s == "":
        #     return True
        # while i < len(t):
        #     if t[i] == s[j]:
        #         print(j)
        #         j += 1
        #         if j == len(s):
        #             return True
        #     i += 1
        # return False

        # this is the same and more concise:
        i, j = 0, 0
        while i < len(t) and j < len(s):
            if s[j] == t[i]:
                j += 1
            i += 1
        return j == len(s)

# @lc code=end
