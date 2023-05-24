#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
class Solution:    
    def numDecodings(self, s: str) -> int:
        # def isValid(str):
        #     if str[0] == '0':
        #         return False
        #     return True
        
        # def dfs(start, path):
        #     if start == len(s):
        #         res.append(''.join(path))
        #         return 
            
        #     for i in s:
        #         if isValid

        #  With n digits, there are O(2^n) nodes in the state-space tree.
        #  We do O(1) operation for each node so the overall time complexity is O(2^n).
        memo = {}

        def dfs(start_index):
            if start_index in memo:
                return memo[start_index]
            if start_index == len(s):
                return 1

            ways = 0
            # can't decode string with leading 0
            if s[start_index] == '0':
                return ways
            # decode one digit
            ways += dfs(start_index + 1)
            # decode two digits
            if 10 <= int(s[start_index: start_index + 2]) <= 26:
                ways += dfs(start_index + 2)
            memo[start_index] = ways
            return ways

        return dfs(0)
    
        # The time complexity of the memoization solution is the size of the memo array O(n) multiplied by the number of operations per state which is O(1). 
        # So the overall time complexity is O(n).
# @lc code=end

