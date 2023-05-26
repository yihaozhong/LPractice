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
    
    # O(n⋅2^n): in the worst case (array consists of nnn distinct elements), the total number of recursive function calls will be 2 ^ n 
    # for each function call, it is O(n) for path operations

    # Space complexity: O(n)
    # The recursion call stack occupies at most O(n)
 

 # sol 2: cascading (adding) , O(n⋅2^n), O(n⋅2^n)
#  def subsets(self, nums: List[int]) -> List[List[int]]:
#         n = len(nums)
#         output = [[]]
        
#         for num in nums:
#             output += [curr + [num] for curr in output]
        
#         return output
# @lc code=end
