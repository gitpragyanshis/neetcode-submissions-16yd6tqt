# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result
            
        q = deque([root])

        while q:
            curr_l = len(q)
            temp_r = []
            for i in range(curr_l):
                item = q.popleft()
                temp_r.append(item.val)

                if item.left:
                    q.append(item.left)
                
                if item.right:
                    q.append(item.right)
            
            result.append(temp_r)
        
        return result