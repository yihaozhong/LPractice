#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = 0
    curDepth = 0
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # def traverse(root):
        #     # base
        #     if(root is None):
        #         return 
            
        #     # pre-order
        #     self.curDepth += 1

        #         # if this is the end leaf
        #     if (root.left is None) and (root.right is None):
        #         self.res = max(self.res, self.curDepth)
            
        #     traverse(root.left)
        #     traverse(root.right)

        #     # post-order
        #     self.curDepth -= 1
        
        # traverse(root)

        # return self.res

        def traverse(root):
            if root is None:
                return 0
            return max(traverse(root.left), traverse(root.right)) + 1
        return traverse(root) if root else 0

    # O(N)
    # O(1)
        
# @lc code=end

