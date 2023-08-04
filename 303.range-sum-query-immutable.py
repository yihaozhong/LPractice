#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#

# @lc code=start
class NumArray:
    preSum = None

    def __init__(self, nums: List[int]):
        self.preSum = [0] * (len(nums)+1)
        for i in range(1, len(self.preSum)):
            self.preSum[i] = (self.preSum[i-1] + nums[i-1])
        return None

    def sumRange(self, left: int, right: int) -> int:
        return self.preSum[right+1] - self.preSum[left]

    # O(1) per queries, O(N) pre-computation
    # O(n) space

    # revisit 8/4
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end
