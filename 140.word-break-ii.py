#
# @lc app=leetcode id=140 lang=python3
#
# [140] Word Break II
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = {}
        def dfs(start, path):
            if start == len(s):
                #print(path)
                result.append(' '.join(path))
                return


            for w in wordDict:
                if s[start:].startswith(w):
                    #print("start and w are ", s[start:], w)
                    #print("path is ", path) 
                    dfs(start + len(w), path+[w])
    
        result = []
        dfs(0, [])
        return result
# @lc code=end
