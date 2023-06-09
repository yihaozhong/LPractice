#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        original_len, check_len = len(s), len(p)
        if original_len < check_len:
            return []

        res = []
        # stores the frequency of each character in the check string
        check_counter = [ 0 ] * 26
        # stores the frequency of each character in the current window
        window = [ 0 ] * 26
        a = ord('a')  # ascii value of 'a'
        # first window
        for i in range(check_len):
            check_counter[ord(p[i]) - a] += 1
            window[ord(s[i]) - a] += 1
        if window == check_counter:
            res.append(0)

        for i in range(check_len, original_len):
            window[ord(s[i - check_len]) - a] -= 1
            window[ord(s[i]) - a] += 1
            if window == check_counter:
                res.append(i - check_len + 1)
        return res

# O(N) and O(1)
# @lc code=end

