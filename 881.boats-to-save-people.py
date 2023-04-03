#
# @lc app=leetcode id=881 lang=python3
#
# [881] Boats to Save People
#

# @lc code=start
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        lo, hi = 0, len(people)-1
        ans = 0
        while lo <= hi:
            if people[lo] + people[hi] > limit:
                hi -= 1
            else:
                lo += 1
                hi -= 1
            ans += 1
        return ans
# @lc code=end

