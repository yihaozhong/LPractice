#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#

# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # two pointer left right
        
        left = 0
        right = len(s) - 1

        while(left < right):
            # do the swap
            temp = s[left]
            s[left] = s[right]
            s[right] = temp

            # move the pointer
            left += 1
            right -= 1


        
# @lc code=end

