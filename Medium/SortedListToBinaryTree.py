# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        return self.sortedArrayToBST(nums)
        
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return
        elif len(nums) == 1:
            return TreeNode(nums[0])
        
        midpoint = len(nums) // 2
        root = TreeNode(nums[midpoint])
        
        left_half = nums[:midpoint]
        right_half = nums[midpoint + 1:]
        
        root.left = self.sortedArrayToBST(left_half)
        root.right = self.sortedArrayToBST(right_half)
        
        return root
