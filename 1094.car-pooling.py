#
# @lc app=leetcode id=1094 lang=python3
#
# [1094] Car Pooling
#

# @lc code=start
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        #1 <= trips.length <= 1000
        ans = [0] * 1001
        for value, start, end in trips:
            if value > capacity:
                return False
            ans[start] += value
            if end < 1001:
                ans[end] -= value

        for i in range(1, 1001):
            ans[i] += ans[i-1]
            if ans[i] > capacity:
                return False
        return True 
        #Time complexity: O(max(N,1001))\mathcal{O}(max(N, 1001))O(max(N,1001)) since we need to iterate over trips and then iterate over our 1001 buckets.

        #Space complexity : O(1001)=O(1)\mathcal{O}(1001)=\mathcal{O}(1)O(1001)=O(1) since we have 1001 buckets.

        # bucket sort
# @lc code=end

