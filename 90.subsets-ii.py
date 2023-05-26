#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtracking(start, path):
            # 前序位置，每个节点的值都是一个子集
            result.append(path[:])
            for i in range(start, len(nums)):
                # 剪枝逻辑，值相同的相邻树枝，只遍历第一条
                if i > start and nums[i-1] == nums[i]:
                    continue
                path.append(nums[i])
                backtracking(i+1 , path)
                path.pop()
        nums.sort()
        result = []
        backtracking(0, [])
        return result
    

    # O(n⋅2^n): in the worst case (array consists of nnn distinct elements), the total number of recursive function calls will be 2 ^ n 
    # for each function call, it is O(n) for path operations

    # Space complexity: O(n)
    # The recursion call stack occupies at most O(n)
# @lc code=end

