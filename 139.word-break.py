#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def dfs(start):
            if start == len(s):
                return True
            
            if start in memo:
                return memo[start]
            
            ans = False
            for w in wordDict:
                if s[start:].startswith(w):
                    ans = ans or dfs(start+len(w))
            
            memo[start] = ans
            return ans
        return dfs(0)
# @lc code=end

