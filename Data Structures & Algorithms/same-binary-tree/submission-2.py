# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q = deque([(p,q)])

        while q:
            left, right = q.popleft()

            if not left and not right:
                continue
            
            if not left or not right:
                return False

            if left.val != right.val:
                return False
            
            
            q.append((left.left, right.left))
            q.append((left.right, right.right))
        
        return True
