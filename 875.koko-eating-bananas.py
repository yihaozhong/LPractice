#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def feasible(speed):
            return sum(math.ceil(pile / speed) for pile in piles) <= h  # slower
            # return sum((pile - 1) / speed + 1 for pile in piles) <= h  # faster
         # Iterate over the piles and calculate hour_spent.
            # We increase the hour_spent by ceil(pile / middle)
        # for pile in piles:
        #     hour_spent += math.ceil(pile / middle)

        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left
    
    #  The initial search space is from 1 to m, 
    #  it takes logm comparisons to reduce the search space to 1.
# @lc code=end
