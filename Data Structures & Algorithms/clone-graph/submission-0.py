"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        s = {}
        s[None] = None
        def dfs(node):
            if not node:
                return None

            if node in s:
                return s[node]

            # clone current node
            s[node] = Node(node.val)

            # clone neighbors
            for n in node.neighbors:
                s[node].neighbors.append(dfs(n))

            return s[node]

                
        dfs(node)
        return s[node]