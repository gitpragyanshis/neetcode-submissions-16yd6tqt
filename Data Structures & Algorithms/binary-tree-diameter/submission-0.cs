/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

public class Solution {
    public int DiameterOfBinaryTree(TreeNode root) {
        int res = 0;
        DiameterOfBinaryTree(root, ref res);
        return res;

    }
    public int DiameterOfBinaryTree(TreeNode root, ref int length)
    {
        if(root == null)
        {
            return 0;
        }

        int left = DiameterOfBinaryTree(root.left, ref length);
        int right = DiameterOfBinaryTree(root.right, ref length);

        length = Math.Max(length, left + right);
        
        return Math.Max(left, right) + 1;
    }
}
