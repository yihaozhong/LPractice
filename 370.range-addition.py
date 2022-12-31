#
# @lc app=leetcode id=370 lang=python3
#
# [370] Range Addition
#

# @lc code=start
class Solution:
    
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        ans = [0] * length
        for start, end, value in updates:
            ans[start] += value
            end += 1
            if end < len(ans):
                ans[end] -= value

        for i in range(1, len(ans)):
            ans[i] += ans[i-1]

        return ans

        #Time complexity : O(n+k). Each of the kkk update operations is done in constant O(1)O(1)O(1) time. The final cumulative sum transformation takes O(n) time always.

        #Space complexity : O(1)O(1)O(1). No extra space required.



# @lc code=end

