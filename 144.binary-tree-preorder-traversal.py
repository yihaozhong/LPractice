#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def traverse(root):
            # base case
            if(root is None):
                return
            res.append(root.val)
            traverse(root.left)
            traverse(root.right)
        
        traverse(root)
        return res

    # O(N)
    # O(N)

# @lc code=end

