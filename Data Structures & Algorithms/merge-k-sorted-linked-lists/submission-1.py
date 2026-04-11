# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        dummy = result = ListNode(-1)

        # add initial items to the heap
        for n in lists:
            heapq.heappush(heap, HeapNode(n))
        
        while heap:
            h_node = heapq.heappop(heap)
            result.next = h_node.node
            if h_node.node.next:
                heapq.heappush(heap, HeapNode(h_node.node.next))
            result = result.next
        

        return dummy.next

class HeapNode:
    def __init__(self, node: ListNode):
        self.node = node
    def __lt__(self, other: ListNode):
        return self.node.val < other.node.val
