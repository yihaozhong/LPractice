#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root, maxDepth):
            if root is None:
                return maxDepth
            left = dfs(root.left, maxDepth + 1)
            right = dfs(root.right, maxDepth + 1)
            
            if abs(left - right) > 1:
                return -1
                
            return max(left, right)
                
        return dfs(root, 0) != -1
        
# @lc code=end

