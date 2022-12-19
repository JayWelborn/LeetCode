# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    @staticmethod
    def value_and_remainder(val1: int = 0, val2: int = 0, remainder = 0):
        ret = val1 + val2 + remainder
        remainder = 0
        if ret >= 10:
            ret = ret % 10
            remainder = 1
        return ret, remainder
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        val = (l1.val + l2.val) % 10
        remainder = (l1.val + l2.val) // 10
        head = ListNode(val=val)
        tail = head
        l1 = l1.next
        l2 = l2.next

        while l1 and l2:
            val, remainder = self.value_and_remainder(val1=l1.val, val2=l2.val, remainder=remainder)
            new_node = ListNode(val=val, next=None)
            tail.next = new_node
            tail = new_node
            l1 = l1.next
            l2 = l2.next

        remaining = l1 or l2
        
        while remaining:
            val, remainder = self.value_and_remainder(val1=remaining.val, remainder=remainder)
            new_node = ListNode(val=val, next=None)
            tail.next = new_node
            tail = new_node
            remaining = remaining.next

        if remainder:
            tail.next = ListNode(val=remainder, next=None)
        
        return head
