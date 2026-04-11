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
    public List<List<int>> LevelOrder(TreeNode root) {
        var queue = new Queue<TreeNode>();
        var result = new List<List<int>>();
        if(root != null)
        {
            queue.Enqueue(root);
        }

        while(queue.Any())
        {
            var currentCount = queue.Count();
            var tempResult = new List<int>();
            while(currentCount > 0)
            {
                var item = queue.Dequeue();
                tempResult.Add(item.val);

                if(item.left != null) queue.Enqueue(item.left);
                if(item.right != null) queue.Enqueue(item.right); 

                currentCount--;
            }

            result.Add(tempResult);
        }

        return result;
    }
}
