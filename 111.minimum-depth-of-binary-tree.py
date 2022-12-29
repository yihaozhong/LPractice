#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return  0
        q = Queue()
        q.put(root)
        # initialize the depth
        depth = 1

        while((q.empty() == False)):
            sz = q.qsize()

            # iterate every node in this level
            for i in range(sz):
                cur = q.get()
                if cur.left is None and cur.right is None:
                    return depth
                if cur.left is not None:
                    q.put(cur.left)
                if cur.right is not None:
                    q.put(cur.right)
            depth += 1
        return depth
        
# @lc code=end

