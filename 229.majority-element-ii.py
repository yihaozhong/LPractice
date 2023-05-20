#
# @lc app=leetcode id=229 lang=python3
#
# [229] Majority Element II
#

# @lc code=start
"""
There can be at most one majority element which is more than ⌊n/2⌋ times.
There can be at most two majority elements which are more than ⌊n/3⌋ times.
There can be at most three majority elements which are more than ⌊n/4⌋ times.

"""
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        curr1, cnt1 = None, 0
        curr2, cnt2 = None, 0

        # 1st pass
        for n in nums:
            if curr1 == n:
                cnt1 += 1
            elif curr2 == n:
                cnt2 += 1
            elif cnt1 == 0:
                curr1 = n
                cnt1 += 1
            elif cnt2 == 0:
                curr2 = n
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        # 2nd pass
        result = []
        for c in [curr1, curr2]:
            if nums.count(c) > len(nums)//3:
                result.append(c)
        return result
# @lc code=end

