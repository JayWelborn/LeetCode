# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys
class Solution:
    prev = -sys.maxsize
    minDiff = sys.maxsize
    def minDiffInBST(self, root: TreeNode) -> int:
        if not root:
            return
        
        self.minDiffInBST(root.left)
        
        self.minDiff = min(self.minDiff, root.val - self.prev)
        self.prev = root.val
        
        self.minDiffInBST(root.right)
        
        return self.minDiff
