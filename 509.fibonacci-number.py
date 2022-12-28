#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution:
    

    # def fib(self, n: int) -> int:

    #     def helper(memo, n):
    #         # base case
    #         if n == 0 or n ==1:
    #             return n

    #         # dp[i-1] and dp[i-2]
    #         if memo[n] != 0:
    #             return memo[n]
            
    #         memo[n] = helper(memo, n-1) + helper(memo, n-2)
    #         return memo[n]

    #     # create a memo 
    #     memo = [0] * (n+1)
    #     return helper(memo, n)
    #这种解法是「自顶向下」进行「递归」求解，我们更常见的动态规划代码是「自底向上」进行「递推」求解
        
        
    def fib(self, n: int) -> int:
        if n == 0:
            return n
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-2] + dp[i-1]
        return dp[n]

    

    
    

        
# @lc code=end

