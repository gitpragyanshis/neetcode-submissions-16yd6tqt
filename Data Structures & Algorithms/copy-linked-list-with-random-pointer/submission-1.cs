/*
// Definition for a Node.
public class Node {
    public int val;
    public Node next;
    public Node random;
    
    public Node(int _val) {
        val = _val;
        next = null;
        random = null;
    }
}
*/

public class Solution {
    public Node copyRandomList(Node head) {
        if(head == null) return null;
        var set = new Dictionary<Node, Node>();
        var temp = new Node(-1);
        temp.next = head;        
        while(head != null)
        {
            var copyNode = new Node(head.val);
            set.Add(head, copyNode);
            head = head.next;
        }

        head = temp.next;        

        while(head != null)
        {            
            set[head].next = head.next == null ? null : set[head.next];
            set[head].random = head.random == null ? null : set[head.random];

            head = head.next;
        }

        return set[temp.next];
    }
}
