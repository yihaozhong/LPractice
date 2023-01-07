#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # to construct a tree, root -> left -> right

        # find the root, which is the first of preorder

        # inorder = [lf, lf, lf, root, rt, rt, rt]
        # preorder = [root, lf, lf, lf, rt, rt, rt]

        # left size of preorder = index of root in in order - inorder start
        
        
        def array_to_tree(left, right):
            nonlocal preorder_index
            if left > right:
                return None
            root_value = preorder[preorder_index]
            root = TreeNode(root_value)
            preorder_index += 1

            root.left = array_to_tree(left, inorder_index_map[root_value] - 1)
            root.right = array_to_tree(inorder_index_map[root_value] + 1,right)

            return root

        preorder_index = 0
        # build a hashmap to store the value -> index relations
        inorder_index_map = {}

        for index, value, in enumerate(inorder): #preorder
            inorder_index_map[value] = index


        return array_to_tree(0, len(preorder) - 1)

        # O(N)
        # O(N)
# @lc code=end

