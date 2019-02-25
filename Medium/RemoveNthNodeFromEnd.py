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
    
    
    
"""
Two-Pointer solution

def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0)
    dummy.next = head
    current = dummy
    prev = dummy
    for i in range(n + 1):
        current = current.next

    while current:
        prev = prev.next
        current = current.next

    prev.next = prev.next.next
    return dummy.next
 """
