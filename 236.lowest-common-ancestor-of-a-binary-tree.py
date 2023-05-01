#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        boolQ = False
        boolP = False
        def traverse(root):
            nonlocal boolQ, boolP
            if root is None:
                return root

            if (root.val == p.val):
                boolP = True
                return root

            if (root.val == q.val):
                boolQ = True
                return root

            left = traverse(root.left)
            right = traverse(root.right)

            print("p is:" + str(boolP) + " q is:" +
                  str(boolQ) + " " + str(root.val))
            if left and right:
                return root
            if left:
                return left
            if right:
                return right
            return None

            
        return traverse(root)
# @lc code=end
