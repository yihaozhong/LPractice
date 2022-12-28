#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    
    def coinChange(self, coins: List[int], amount: int) -> int:

        
        # # dp function
        # def dp(coins, amount):
        #     # base case
        #     if amount == 0:
        #         return 0
        #     if amount <= 0:
        #         return -1
            
        #     res = amount + 1
        #     # subproblem
        #     for i in coins:
        #         subproblem = dp(coins, amount-i)
        #         # if there is no sol, continue
        #         if subproblem == -1:
        #             continue
        #         res = min(res, subproblem+1)
        #     return res if res != (amount+1) else -1

        # return dp(coins, amount)
        # O(K^n), amount is n, k coins

        # dp function with memo
        # dp(n) 表示，输入一个目标金额 n，返回凑出目标金额 n 所需的最少硬币数量
        # top down
        # memo = [-666] * (amount+1)
        # def dp(coins, amount):
        #     # base
        #     if amount == 0:
        #         return 0
        #     if amount <0:
        #         return -1

        #     if memo[amount] != (-666):
        #         return memo[amount]

        #     res = amount + 1
        #     for i in coins:
        #         subproblem = dp(coins, amount-i)
        #         if subproblem == -1:
        #             continue
        #         res = min(res,subproblem +1)  
        #     memo[amount] = res if res !=(amount+1) else -1

        #     return memo[amount]
        
        # return dp(coins, amount)
        # O(K*N)
                

        # dp array
        # bottom down 
       
        if amount < 0:
            return -1
        dp = [amount+1] * (amount + 1)
        dp[0] = 0

        for i in range (1, amount+1):
            for coin in coins:
                if (i - coin) < 0:
                    continue
                dp[i] = min(dp[i], 1 + dp[i - coin])
        return dp[amount] if dp[amount] != (amount +1) else -1 
        # O(K*N)


# @lc code=end

