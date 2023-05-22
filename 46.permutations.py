#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

"""

# iterate all possible candidates.
    for next_candidate in list_of_candidates:
        if is_valid(next_candidate):
            # try this partial candidate solution
            place(next_candidate)
            # given the candidate, explore further.
            backtrack(next_candidate)
            # backtrack
            remove(next_candidate)
"""


# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(start, path, used):
            if start == len(nums):
                result.append(path[:])
                return
            for i, num in enumerate(nums):
                if not used[i]:
                    path.append(num)
                    used[i] = True
                    dfs(start+1, path, used)
                    # remove letter from permutation, mark letter as unused
                    path.pop()
                    used[i] = False

        result, use = [], [False] * len(nums)
        dfs(0, [], use)
        return result

# O(N!)

"""
def backtrack(first = 0):
            # if all integers are used up
            if first == n:  
                output.append(nums[:])
            for i in range(first, n):
                # place i-th integer first 
                # in the current permutation
                nums[first], nums[i] = nums[i], nums[first]
                # use next integers to complete the permutations
                backtrack(first + 1)
                # backtrack
                nums[first], nums[i] = nums[i], nums[first]
        
        n = len(nums)
        output = []
        backtrack()
        return output

"""
# @lc code=end

