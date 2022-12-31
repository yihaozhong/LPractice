#
# @lc app=leetcode id=1109 lang=python3
#
# [1109] Corporate Flight Bookings
#

# @lc code=start
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0] * n
        for start, end, value in bookings:
            ans[start-1] += value
            if end < n:
                ans[end] -= value
        
        for i in range(1,n):
            ans[i] += ans[i-1]

        return ans

        
# @lc code=end

