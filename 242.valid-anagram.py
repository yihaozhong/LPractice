#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        myCounter1 = Counter(s)
        myCounter2 = Counter(t)

        return myCounter1 == myCounter2
    
        # return sorted(s) == sorted(t)

        # dic1, dic2 = [0]*26, [0]*26
        # for item in s:
        #     dic1[ord(item)-ord('a')] += 1
        # for item in t:
        #     dic2[ord(item)-ord('a')] += 1
        # return dic1 == dic2

        
# @lc code=end

