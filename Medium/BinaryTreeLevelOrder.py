# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        current_level = [root]
        next_level = [x for x in [root.left, root.right] if x]
        level_order = []
        level = 0
        while(current_level):
            level_order.append([])
            for node in current_level:
                level_order[level].append(node.val)
            level += 1
            current_level = next_level
            next_level = []
            for node in current_level:
                if node and node.left:
                    next_level.append(node.left)
                if node and node.right:
                    next_level.append(node.right)
                    
        return level_order
