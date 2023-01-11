#
# @lc app=leetcode id=780 lang=python3
#
# [780] Reaching Points
#

# @lc code=start
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx >= sx + ty or ty >= sy + tx: # make sure we can still make substractions
            if tx > ty:
                tx = sx + (tx -sx)%ty # the smallest we can get by deducting ty from tx
            else:
                ty = sy + (ty - sy) %tx # the smallest we can get by subtracting tx from ty

        return tx == sx and ty == sy
# @lc code=end

