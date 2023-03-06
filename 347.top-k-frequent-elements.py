#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myCounter = collections.Counter(nums)
        myCounter = dict(sorted(myCounter.items(), key =lambda item: item[1], reverse= True))
        return list(myCounter.keys())[:k]

# @lc code=end

