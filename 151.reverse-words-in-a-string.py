#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        def reserve(s1: str):
            left = 0
            right = len(s1) - 1
            while(left<right):
                temp = s1[left]
                s1[left] = s1[right]
                s1[right] = temp
                left +=1
                right -=1
        reserve(s)
        strg = s.split(" ")
        result = ""
        for i in range(len(strg)):
            reserve(strg[i])
            result+= i
            if i != len(strg)-1:
                result += " "
        return result
# @lc code=end

