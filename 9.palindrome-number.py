#
# @lc app=leetcode id=9 lang=python
#
# [9] Palindrome Number
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x <0:
            return False
        temp = x
        y = 0
        while (temp > 0):
            last_digit = temp % 10
            y = y*10 + last_digit
            temp = temp //10
        return y == x

#print(Solution().isPalindrome(121))
        
# @lc code=end

