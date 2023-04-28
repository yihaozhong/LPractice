#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        stack = []
        def traverse(root):
            if root is None:
                stack.append('None')
                return None
            stack.append(str(root.val))
            traverse(root.left)
            traverse(root.right)

        traverse(root)
        #print(stack)
        return ' '.join(stack)
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        def dfs(data):

            if data[0] == 'None':
                data.pop(0)
                return None
            root = TreeNode(int(data[0]))
            data.pop(0)
            root.left = dfs(data)
            root.right = dfs(data)
            return root
        root = dfs(data.split(" "))
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

