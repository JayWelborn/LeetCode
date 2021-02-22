# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import math
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        def isValid(node, leftVal, rightVal):
            if not node:
                return True
            if not (leftVal < node.val < rightVal):
                return False
            
            return isValid(node.left, leftVal, node.val) and isValid(node.right, node.val, rightVal)
        
        return isValid(root, -math.inf, math.inf)
