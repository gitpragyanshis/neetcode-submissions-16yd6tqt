/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

public class Solution {
    public void ReorderList(ListNode head) {
        var mid = MiddleNode(head);
        var second = mid.next;
        mid.next = null;
        var reversed = ReverseList(second);
        var dummy = head;

        while(head != null && reversed != null)
        {
            var temp = head.next;
            var temp2 = reversed.next;
            head.next = reversed;            
            reversed.next = temp;
            reversed = temp2;
            head = temp;
        }
    }

    public ListNode ReverseList(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;

        while(curr != null)
        {
            var next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;            
        }

        return prev;
    }

    public ListNode MiddleNode(ListNode head) {
        var slow = head;
        var fast = head;

        while(fast != null && fast.next != null)
        {
            slow = slow.next;
            fast = fast.next.next;
        }
        
        return slow;
    }
}
