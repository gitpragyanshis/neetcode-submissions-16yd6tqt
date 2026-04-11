# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_q = deque([(p, q)])

        while p_q:
            i_p, i_q = p_q.popleft()

            if i_p is None and i_q is None:
                continue
            
            if i_p is None or i_q is None:
                return False
            
            if i_p.val != i_q.val:
                return False
            
            p_q.append((i_p.left, i_q.left))
            p_q.append((i_p.right, i_q.right))
        
        return True

