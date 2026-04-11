# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
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
        
        if not root:
            return subRoot == None

        if isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        

