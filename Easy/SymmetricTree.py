# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isMirror(left: TreeNode, right: TreeNode):
            
            # Two null values are mirrors
            if left is None and right is None:
                return True
            
            # If only one value is null, these trees do not mirror each other
            if left is None or right is None:
                return False
            
            # If the values are not equal, the trees do not mirror each other
            if left.val != right.val:
                return False
            
            # If left.left mirrors right.right, and left.right mirrors right.left,
            # the subtrees mirror each other
            return isMirror(left.left, right.right) and isMirror(left.right, right.left)
            
        return isMirror(root, root)
        
