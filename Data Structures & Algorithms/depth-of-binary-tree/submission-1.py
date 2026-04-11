# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.max_depth = 0
        self.calculate_max_depth(root, 1)

        return self.max_depth

    def calculate_max_depth(self, root: Optional[TreeNode], depth: int):
        if not root:
            return None
        
        self.max_depth = max(depth, self.max_depth)
        self.calculate_max_depth(root.left, depth + 1)
        self.calculate_max_depth(root.right, depth + 1)
        