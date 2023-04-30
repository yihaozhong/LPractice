#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # def traverse(root):
        #     if root is None:
        #         return
        #     root.left, root.right = root.right, root.left
        #     traverse(root.left)
        #     traverse(root.right)

        # traverse(root)
        # return root


        def traverse(root):
            if root is None:
                return None
            root.left, root.right = root.right, root.left
            traverse(root.left)
            traverse(root.right)
        
        traverse(root)

        return root

    # O(N)
    # O(1)

    
# @lc code=end

