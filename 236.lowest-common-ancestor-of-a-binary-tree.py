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
        """
        解题思路：每个节点要知道什么、做什么：什么时候做
        遍历or递归
        要知道自己的子树里是否有这两个数字->递归
        要做什么：返回自己子树是否有这两个数字->递归
        什么时候做：后序遍历，传递子树信息

        自下而上，这个函数就返回自己左右子树满足条件的node：返回自己或者不为None的一边。base case就是找到了
        如果一个节点能够在它的左右子树中分别找到 p 和 q，则该节点为 LCA 节点。

        时间：O(N)
        空间：O(N)
        """
        if root is None:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # 后序遍历
        if root == p or root == q: # Case 1：公共祖先就是我自己，也可以放在前序位置（要确保p,q在树中）
            return root
        
        if left and right: # Case 2：自己子树包含这两个数
            return root
        else:
            return left or right # Case 3：


        
        # boolQ = False
        # boolP = False
        # def traverse(root):
        #     nonlocal boolQ, boolP
        #     if root is None:
        #         return root

        #     if (root.val == p.val):
        #         boolP = True
        #         return root

        #     if (root.val == q.val):
        #         boolQ = True
        #         return root

        #     left = traverse(root.left)
        #     right = traverse(root.right)

        #     print("p is:" + str(boolP) + " q is:" +
        #           str(boolQ) + " " + str(root.val))
        #     if left and right:
        #         return root
        #     if left:
        #         return left
        #     if right:
        #         return right
        #     return None

            
        # return traverse(root)
# @lc code=end
