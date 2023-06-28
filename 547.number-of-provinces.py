#
# @lc app=leetcode id=547 lang=python3
#
# [547] Number of Provinces
#

# @lc code=start
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        seen = set()
        def dfs(node):
            for nei, adj in enumerate(isConnected[node]):
                if adj and nei not in seen:
                    seen.add(nei)
                    dfs(nei)
    
        ans = 0
        for i in range(N):
            if i not in seen:
                dfs(i)
                ans += 1
        return ans
# @lc code=end

