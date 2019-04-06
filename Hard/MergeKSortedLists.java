/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists.length == 0) {
            return null;
        } else if (lists.length == 1) {
            return lists[0];
        } else if (lists.length == 2) {
            return mergeTwoLists(lists[0], lists[1]);
        }
        
        int mid = lists.length / 2;
        
        ListNode[] left = Arrays.copyOfRange(lists, 0, mid);
        ListNode[] right = Arrays.copyOfRange(lists, mid, lists.length);
        
        return this.mergeTwoLists(mergeKLists(left), mergeKLists(right));
    }
    
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if (l1 == null & l2 == null) {
            return null;
        } else if (l2 == null) {
            return l1;
        } else if (l1 == null) {
            return l2;
        }
        
        if (l1.val < l2.val) {
            l1.next = mergeTwoLists(l1.next, l2);
            return l1;
        }
        
        l2.next = mergeTwoLists(l1, l2.next);
        return l2;
    }
}
