# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        if root is None:
            return ""
        left = self.binaryTreePaths(root.left)
        right = self.binaryTreePaths(root.right)
        if left:
            for path in left:
                paths.append(f"{root.val}->{path}")
        if right:
            for path in right:
                paths.append(f"{root.val}->{path}")
        if not left and not right:
            paths = [f"{root.val}"]
        return paths
