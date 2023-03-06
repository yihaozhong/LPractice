#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start

from collections import Counter

class Solution:
    def encode(self, s):
        count = [0] *26
        for c in s:
            delta = ord(c) - ord('a')
            count[delta] += 1
        return tuple(count) #''.join(str(x) for x in count)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for i in strs:
            code = self.encode(i)
            if code not in dict:
                dict[code] = []
            dict[code].append(i)

        res = []
        for g in dict.values():
            res.append(g)
        return res
        
        # ans = collections.defaultdict(list)
        # for s in strs:
        #     count = [0] * 26
        #     for c in s:
        #         count[ord(c) - ord('a')] += 1
        #     ans[tuple(count)].append(s)
        # return ans.values()

# @lc code=end

