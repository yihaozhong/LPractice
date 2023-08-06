#
# @lc app=leetcode id=370 lang=python3
#
# [370] Range Addition
#

# @lc code=start
class Solution:
    '''
    差分数组和原数组包含的信息是相同的，只是形式不同而已。差分数组中每一个元素都是前面的元素的和，它自带递推的结构。
    递推的特点是只需要知道第一个元素的信息就可以得到后面的信息，即第一个对象的信息会影响后面的所有对象的信息。而常规数组的各个元素之间的关系是独立的。
    '''
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        ans = [0] * length

        # treat ans as a diff array
        for start, end, value in updates:
            ans[start] += value
            end += 1
            if end < len(ans):
                ans[end] -= value

        # from diff array to original array, reverse construct
        for i in range(1, len(ans)):
            ans[i] += ans[i-1]

        return ans

        #Time complexity : O(n+k). Each of the kkk update operations is done in constant O(1)O(1)O(1) time. The final cumulative sum transformation takes O(n) time always.

        #Space complexity : O(1)O(1)O(1). No extra space required.



# @lc code=end

