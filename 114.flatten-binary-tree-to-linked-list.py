#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 定义：输入节点 root 然后 root 为根的二叉树就会被拉平为一条链表

        # 1. use flatten(x.left) and flattern(x.right) to flattern x's left and right
        # connect x.right to x.left, and let the whole x.left become x.right

        #base
        if root is None:
            return
        # flatten the tree
        self.flatten(root.left)
        self.flatten(root.right)


        # root.left.right = root.right
        # root.right = root.left
        # root.left = None


        left = root.left
        right = root.right

        root.left = None
        root.right = left

        p = root
        while(p.right):
            p = p.right

        p.right = right

    # 
# @lc code=end

