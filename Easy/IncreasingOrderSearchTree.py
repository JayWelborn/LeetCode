# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def buildSortedList(self, node: TreeNode) -> List[TreeNode]:
        if not node:
            return []
        cache = self.buildSortedList(node.left)
        node.left = None
        cache.append(node)
        cache += self.buildSortedList(node.right)
        node.right = None
        return cache
    
    def increasingBST(self, root: TreeNode) -> TreeNode:
        inOrderCache = self.buildSortedList(root)
        for i in range(len(inOrderCache) - 1):
            inOrderCache[i].left = None
            inOrderCache[i].right = inOrderCache[i + 1]
            
        inOrderCache[-1].right = None
        return inOrderCache[0]
        
