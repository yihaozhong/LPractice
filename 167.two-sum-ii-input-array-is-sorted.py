#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#
# f it is less than target, we increase the smaller index by one. 
# If it is greater than target, we decrease the larger index by one. 
# Move the indices and repeat the comparison until the solution is found.
# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # left right pointer
        left = 0
        right = len(numbers) - 1

        
        while (left < right):
            sum = numbers[left] + numbers[right]
            if (sum < target):
                left += 1
            elif (sum > target):
                right -=1
            else:
                return [left+1, right+1]

    # revisit 8/2
# @lc code=end

