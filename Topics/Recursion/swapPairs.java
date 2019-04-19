/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode swapPairs(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        
        ListNode two = head.next, one = head;
        head = head.next;
        one.next = swapPairs(two.next);
        two.next = one;
        one = one.next;
        if (one != null)
            two = one.next;
        return head;
    }
}
