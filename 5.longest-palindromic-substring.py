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
    '''
    回文串的的长度可能是奇数也可能是偶数，解决该问题的核心是从中心向两端扩散的双指针技巧。

    如果回文串的长度为奇数，则它有一个中心字符；如果回文串的长度为偶数，则可以认为它有两个中心字符。
    
    如果输入相同的 l 和 r，就相当于寻找长度为奇数的回文串，如果输入相邻的 l 和 r，则相当于寻找长度为偶数的回文串
    '''
    # time: O(N^2)
    # space: O(1)

# @lc code=end

