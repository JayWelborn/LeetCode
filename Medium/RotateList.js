/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode}
 */
var rotateRight = function(head, k) {
    let node = head, count = 0;
    while (node !== null) {
        node = node.next;
        count++;
    }
    k %= count;
    if (k == 0 || isNaN(k)) {
        return head;
    }
    
    node = head;
    let prev = null;
    while (count != k) {
        prev = node;
        node = node.next;
        count--;
    }
    prev.next = null;
    
    prev = node;
    while (node.next) {
        node = node.next;
    }
    
    node.next = head;
    return prev
};
