#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPurchase = prices[0]
        maxProfit = 0
        for i in range(1, len(prices)):
            maxProfit = max(maxProfit, prices[i] - minPurchase)
            minPurchase = min(minPurchase, prices[i])
        return maxProfit
        
# @lc code=end

