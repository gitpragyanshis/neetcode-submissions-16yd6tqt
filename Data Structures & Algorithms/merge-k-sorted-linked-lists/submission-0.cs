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
    public ListNode MergeKLists(ListNode[] lists) {
        if(lists.Length == 0)
        {
            return null;
        }

        while(lists.Length > 1)
        {
            var mergedList = new ListNode[((lists.Length + 1)/2)];
            for(int i = 0; i < lists.Length; i += 2)
            {
                var l1 = lists[i];
                var l2 = i+1<lists.Length ? lists[i + 1] : null;

                mergedList[(i/2)] = MergeTwoLists(l1, l2);
            }

            lists = mergedList;
            
        }

        return lists[0];
    }

    public ListNode MergeTwoLists(ListNode list1, ListNode list2) {
        ListNode dummy = new ListNode();
        ListNode node = dummy;

        while(list1 != null && list2 != null)
        {
            if(list1.val < list2.val)
            {
                node.next = list1;
                list1 = list1.next;
            }
            else
            {
                node.next = list2;
                list2 = list2.next;
            }

            node = node.next;
        }

        if(list1 != null)
        {
            node.next = list1;           
        }
        if(list2 != null)
        {
            node.next = list2;            
        }

        return dummy.next;
        
    }
}
