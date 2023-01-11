#
# @lc app=leetcode id=730 lang=python3
#
# [730] Count Different Palindromic Subsequences
#

# @lc code=start

from functools import lru_cache
from collections import defaultdict, deque
class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        M = 10**9 + 7

        fwd = deque()
        dic = defaultdict(lambda: -1)
        for i in range(len(s)-1,-1,-1):
            ch = s[i]
            dic[ch] = i
            fwd.appendleft(dic.copy())

        bwd = []
        dic = defaultdict(lambda: -1)
        for i,ch in enumerate(s):
            dic[ch] = i
            bwd.append(dic.copy())

        @lru_cache(None)
        def dp(i,j):
            if i > j:
                return 1  # empty string
            ans = 1  # empty string
            for l in ('a','b','c','d'):
                m = fwd[i][l]
                n = bwd[j][l]

                if m == -1 or n < i or m > j:
                    continue
                ans += 1  # unique char
                if m < n:
                    ans += dp(m+1,n-1)
            return ans%M

        return dp(0,len(s)-1)-1
# @lc code=end

