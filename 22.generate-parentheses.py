#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start

# When we branch out and generate the edges, 
# we can either add ( and increment openCount or add ) and increment closeCount.
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(start_index, path, open_count, close_count):
            if start_index == n*2:
                result.append(''.join(path))
                return 
            if open_count <n:
                path.append("(")
                dfs(start_index + 1, path, open_count + 1, close_count)
                path.pop()
            if  close_count < open_count: # instead of close_count < n
                path.append(")")
                dfs(start_index + 1, path, open_count, close_count + 1)
                path.pop()

            
        result = []
        dfs(0, [], 0, 0)
        return result
    """
    def dfs(path, open_count, close_count, res):
        if len(path) == 2 * n:
            res.append(''.join(path))
            return
        for parenthesis in ['(', ')']:
          if parenthesis == '(' and open_count >= n:
              continue
          if parenthesis == ')' and close_count >= open_count:
              continue
          path.append(parenthesis)
          if parenthesis == '(':
              open_count += 1
          else:
              close_count += 1
          dfs(path, open_count, close_count, res)
          # reverting the state
          if parenthesis == '(':
              open_count -= 1
          else:
              close_count -= 1
          path.pop()
    
    """
    # There are 2^(2n) = 4^n combinations of possible parentheses. 
    # O(4^n)
# @lc code=end

