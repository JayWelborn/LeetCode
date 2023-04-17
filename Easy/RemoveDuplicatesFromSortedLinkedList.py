class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        while node and node.next:
            next_node = node.next
            while next_node and next_node.val == node.val:
                next_node = next_node.next
            node.next = next_node
            node = node.next

        return head
