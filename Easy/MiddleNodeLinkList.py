# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        count = 0
        node = head
        while node:
            count += 1
            node = node.next
        
        mid = count // 2
        node = head
        for i in range(mid):
            node = node.next
        return node
