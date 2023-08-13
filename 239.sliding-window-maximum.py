#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
from collections import deque
class MonotonicQueue:
    def __init__(self) -> None:
        # 双向链表，支持头部和尾部增删元素
        # 维护其中的元素自尾部到头部单调递增
        self.maxq = deque()

     # 在尾部添加一个元素 n，维护 maxq 的单调性质
    def push(self, n:int) -> None:
        # 将前面小于自己的元素都删除

        while len(self.maxq) > 0 and self.maxq[-1] < n:
            self.maxq.pop()
        self.maxq.append(n)

    def max(self) -> int:
        return self.maxq[0]
    
    # delete n from queue
    def pop(self, n: int) -> None:
        if n == self.maxq[0]:
            self.maxq.popleft()



class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # use monotonic queue, achieving O(1)
        # window = deque()
        window = MonotonicQueue()
        res = []

        for i in range(len(nums)):
            if i < k - 1:
                window.push(nums[i])
            else:
                window.push(nums[i])
                res.append(window.max())
                window.pop(nums[i-k + 1])
        return res


# @lc code=end

