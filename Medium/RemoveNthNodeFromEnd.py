# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        nodes = []
        node = head
        while node:
            nodes.append(node)
            node = node.next
        
        for i in range(n):
            nodes.pop()
        
        if not nodes:
            return head.next
        
        prev = nodes.pop()
        prev.next = prev.next.next
        return head
        
