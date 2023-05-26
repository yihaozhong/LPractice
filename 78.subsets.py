#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtracking(start, path):
            # 前序位置，每个节点的值都是一个子集
            result.append(path[:])

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtracking(i+1, path) # 通过 start 参数控制树枝的遍历，避免产生重复的子集
                path.pop()

        result = []
        backtracking(0, [])
        return result
# @lc code=end
