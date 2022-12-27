# @before-stub-for-debug-begin
from python3problem5 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # we use a two pointer with left right pointer from center

        def expandFromCenter(s, l, r):
            while( (l>= 0) and (r< len(s)) and (s[l] == s[r])):
                l-=1
                r+=1
            return s[l+1: r]
        
        # if we enter l, l -> even palindrom, l, l+1 -> odd 
        
        # loop through the strinf
        result = ""
        for i in range(len(s)):
            str1 = expandFromCenter(s, i, i)
            str2 = expandFromCenter(s, i, i+1)
            temp = str1 if len(str1)>len(str2) else str2
            result = temp if len(temp)>len(result) else result

        return result

    # time: O(N^2)
    # space: O(1)

# @lc code=end

