# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result: List[List[int]] = []

        if not root:
            return result
            
        q = deque([root])

        while q:
            l = len(q)
            temp = []

            for i in range(l):
                curr = q.popleft()

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                    
                temp.append(curr.val)
            result.append(temp)

        return result