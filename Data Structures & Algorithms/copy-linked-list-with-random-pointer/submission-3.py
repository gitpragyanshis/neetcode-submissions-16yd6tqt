"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        m = {}
        m[None] = None

        temp = head

        while head:
            m[head] = Node(head.val)
            head = head.next
        
        # Copy pointer
        head = temp
        while head:
            m[head].next = m[head.next]
            m[head].random = m[head.random]
            head = head.next
        
        return m[temp]


