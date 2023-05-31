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
        # bfs

        # if root is None:
        #     return  0
        # q = Queue()
        # q.put(root)
        # # initialize the depth
        # depth = 1

        # while((q.empty() == False)):
        #     sz = q.qsize()

        #     # iterate every node in this level
        #     for i in range(sz):
        #         cur = q.get()
        #         if cur.left is None and cur.right is None:
        #             return depth
        #         if cur.left is not None:
        #             q.put(cur.left)
        #         if cur.right is not None:
        #             q.put(cur.right)
        #     depth += 1
        # return depth

        # dfs
        res = float("inf")
        def dfs(node = root, level = 0):
            nonlocal res
            if not node:
                res = min(res, level)
                return root
            if node.left is None:
                dfs(node.right, level + 1)
            elif node.right is None:
                dfs(node.left, level + 1)
            else:
                dfs(node.left, level + 1)
                dfs(node.right, level + 1)

        dfs()
        return res
        
# @lc code=end

