#
# @lc app=leetcode id=1328 lang=python3
#
# [1328] Break a Palindrome
#

# @lc code=start
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        left, right = 0, len(palindrome) -1
        str_itr = list(palindrome)
        while left < right:
            if str_itr[left] != "a":
                str_itr[left] = "a"
                return ''.join(str_itr)
            left += 1
            right -= 1
        if len(str_itr) == 1: 
            return ""
        str_itr[-1] = "b"
        return ''.join(str_itr)

# @lc code=end

