# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def get_val(self, ll):
        num = 0
        digits = 0
        while (ll != None):
            num += ll.val * (10**digits)
            digits += 1
            ll = ll.next
        return num
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum = self.get_val(l1) + self.get_val(l2)
        
        ret_list = ListNode(sum % 10)
        next_node = ret_list
        while (sum > 0):
            sum = sum // 10
            if (sum == 0):
                return ret_list
            next_node.next = ListNode(sum % 10)
            next_node = next_node.next
        return ret_list
            
