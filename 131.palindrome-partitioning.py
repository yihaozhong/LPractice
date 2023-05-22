#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def check(s: str):
            first, last = 0, len(s) - 1
            while first < last:
                if s[first] != s[last]:
                    return False
                first += 1
                last -= 1
            return True

        def dfs(start_index, path):
            if start_index == len(s):
                result.append(path)
                return
            for end in range(start_index + 1, len(s) + 1):
                if check(s[start_index: end]):
                    dfs(end, path + [s[start_index: end]])

        result = []
        dfs(0, [])
        return result
    
    #  For each letter in the input string, we can either include it as a previous string or start a new string with it. With those two choices, the total number of operations is 2^n. 
    #  We also need O(n) to check if the string is a palindrome.
    # O(2^N*N) 
# @lc code=end
