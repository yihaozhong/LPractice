#
# @lc app=leetcode id=1438 lang=python3
#
# [1438] Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
#

# @lc code=start
from collections import deque
"""
        use flexible sliding window
        use deque to econimically keep track of the min and max of the window
        both deques MUST include the newest right element
		NOTE: both deques contains the index, NOT the element values 
        deque "desc": elements from high to low. If the right element is the max of the window, then desc only contains the right element
        deque "asc": elements from low to high. if the right is the min of the window, then asc only contains the right element
        
        every time we move the right index
        * we first update the two deques on the new right element
        * we then check max - min = desc[0] - asc[0]. if it is bigger than limit, move the left index until it is NOT bigger than the limit
        * every time we move the left index, if the left index of desc or asc is lower than left, remove them
        """


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # O(n)
        max_len = 1
        asc, desc = deque([0]), deque([0]) # at the start, both deques only contain the first element
        for right in range(1, len(nums)):
            while asc and nums[asc[-1]] > nums[right]:
                asc.pop()
            asc.append(right)

            while desc and nums[desc[-1]] < nums[right]:
                desc.pop()
            desc.append(right)

            while nums[desc[0]] - nums[asc[0]] > limit:
                left += 1
                if desc[0] < left:
                    desc.popleft()
                if asc[0] < left:
                    asc.popleft()
            max_len = max(max_len, right - left + 1)
        return max_len
# @lc code=end

