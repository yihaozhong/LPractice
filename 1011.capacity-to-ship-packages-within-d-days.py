#
# @lc app=leetcode id=1011 lang=python3
#
# [1011] Capacity To Ship Packages Within D Days
#

# @lc code=start
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def feasible(capacity) -> bool:
            day = 1 
            total = 0
            for w in weights:
                total += w
                if total > capacity:
                    # for next round
                    total = w
                    day += 1
                    if day >days:
                        return False
            return True
        
        left, right = max(weights), sum(weights)
        first_index = -1
        while left <= right:
            mid = (left + right) //2

            if feasible(mid):
                first_index = mid
                right = mid - 1
            else:
                left = mid + 1
        return first_index
    
        '''
        the same
        
        while left < right:
            mid = left + (right - left) // 2
        if feasible(mid):
            right = mid
        else:
            left = mid + 1
         return left
        
        '''
# @lc code=end

