# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        if root:
            ret = self.inorderTraversal(root.left)
            ret.append(root.val)
            ret = ret + self.inorderTraversal(root.right)
        return ret
 
