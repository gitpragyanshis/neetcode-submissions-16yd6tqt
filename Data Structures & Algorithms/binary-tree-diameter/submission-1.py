# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        self.find_diameter(root)


        return self.result
    
    def find_diameter(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        left = self.find_diameter(root.left)
        right = self.find_diameter(root.right)
        self.result = max(self.result, left + right)

        return max(left, right) + 1
