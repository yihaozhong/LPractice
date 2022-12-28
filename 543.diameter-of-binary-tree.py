#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxDiameter = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # use post order

        def maxDepth(root):
            if (root is None):
                return 0 

            leftDepth = maxDepth(root.left)
            rightDepth = maxDepth(root.right)
            # post order to calculate the max diameter
            self.maxDiameter = max(self.maxDiameter, rightDepth + leftDepth)
            return 1 + max(leftDepth, rightDepth)

        maxDepth(root)
        return self.maxDiameter



# @lc code=end

