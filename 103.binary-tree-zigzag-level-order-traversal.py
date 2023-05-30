#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result  = []
        if not root:
            return result
        queue = deque([root,])
        flip_flop = True
        while(len(queue) > 0):
            n = len(queue)
            new_level = deque() # use a queue instead of list
            for _ in range(n):
                node = queue.popleft()
                if flip_flop:
                    new_level.append(node.val)
                else:
                    new_level.appendleft(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(new_level)
            flip_flop = not flip_flop
        return result
# @lc code=end

