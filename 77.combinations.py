#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # my sol, wrong
        def dfs(start, path):
            if len(path)== k: # not start == k
                result.append(path[:])
                return
            
            for i in range(start+1, n+1):
                path.append(i)
                dfs(i, path) # not dfs(start+1, path)

                path.pop()
            

        result = []
        dfs(0, [])
        return result

        # def backtrack(first = 1, curr = []):
        #     # if the combination is done
        #     if len(curr) == k:  
        #         output.append(curr[:])
        #     for i in range(first, n + 1):
        #         # add i into the current combination
        #         curr.append(i)
        #         # use next integers to complete the combination
        #         backtrack(i + 1, curr)
        #         # backtrack
        #         curr.pop()
        
        # output = []
        # backtrack()
        # return output
# @lc code=end

