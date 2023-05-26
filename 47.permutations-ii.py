#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtracking(path, used):
            if len(path) == len(nums):
                result.append(path[:])
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]: # i > 0 to avoid 111, 222
                    # 如果前面的相邻相等元素没有用过，则跳过
                    continue
                used[i] = True
                path.append(nums[i])
                backtracking(path, used)
                used[i] = False
                path.pop()
        nums.sort()
        result = []
        backtracking([], [False]*len(nums))
        return result
# @lc code=end

