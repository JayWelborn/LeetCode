# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        tortoise = head
        hair = head.next
        while hair and hair.next and tortoise != hair:
            tortoise = tortoise.next
            hair = hair.next.next
        return tortoise == hair
        
