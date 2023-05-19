#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def traverse(root, minVal, maxVal):
            if root is None:
                return True
            
            if root.val >= maxVal or root.val <= minVal:
                return False
            return traverse(root.left, minVal, root.val) and traverse(root.right, root.val, maxVal)
        return traverse(root, float('-inf'), float('inf'))
    
        # O(N) since we visit each node exactly once.
        # O(N) since we keep up to the entire tree.


        
# @lc code=end

