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

    List<int> result;
    int maxDepth;
    public List<int> RightSideView(TreeNode root) {
        result = new List<int>();
        maxDepth = 0;
        if(root == null) return result;        

        RightSideView(root, 1);

        return result;
    }

    public void RightSideView(TreeNode root, int depth)
    {
        if(root == null)
        {
            return;
        }
        
        if(depth > maxDepth)
        {
            result.Add(root.val);
        }

        maxDepth = Math.Max(depth, maxDepth);

        RightSideView(root.right, depth + 1);
        RightSideView(root.left, depth + 1);        
    }
}
