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
    public int GoodNodes(TreeNode root) {
        if (root == null) {
            return 0;
        }

        int result = 0; 
        int max = root.val;       
        CountGoodNodes(root, max, ref result);

        return result;
    }

    public void CountGoodNodes(TreeNode root, int max, ref int result) {
        if (root == null) {
            return;
        }

        if (root.val >= max) {
            result++;
        }

        max = Math.Max(max, root.val);
        CountGoodNodes(root.left, max, ref result);
        CountGoodNodes(root.right, max, ref result);
    }
}

