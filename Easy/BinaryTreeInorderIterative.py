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
        nodes = []
        current = root
        done = False
        while(not done):
            if current is not None:
                nodes.append(current)
                current = current.left
            else:
                if nodes:
                    current = nodes.pop()
                    ret.append(current.val)
                    current = current.right
                else:
                    done = True
        
        return ret
