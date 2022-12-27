#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

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


# @lc code=end

