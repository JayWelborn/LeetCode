# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        
        def searchHeight(node):
            if not node:
                return 0

            depthLeft = searchHeight(node.left)
            if depthLeft == inf:
                return inf
            
            depthRight = searchHeight(node.right)
            if depthRight == inf:
                return inf
            
            if abs(depthLeft - depthRight) > 1:
                return inf
            
            return max(depthLeft, depthRight) + 1
        
        return searchHeight(root) != inf
