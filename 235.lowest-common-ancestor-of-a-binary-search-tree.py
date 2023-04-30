# @before-stub-for-debug-begin
from python3problem235 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
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
        def traverse(root: 'TreeNode', le: int, ri: int):
            # in order traversal 
            if root is None:
                print("hi")
                return root
            
            if root.val < le:
                
                return traverse(root.right, le, ri)
            
            elif le <= root.val <=ri:
                
                return root

            elif root.val > ri:
                return traverse(root.left, le, ri)

            
        
        if p.val < q.val:
            left = p.val
            right = q.val
        else:
            left = q.val
            right = p.val

        return traverse(root, left, right)
# @lc code=end

