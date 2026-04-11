public class Solution {
    List<List<int>> result;
    public List<List<int>> CombinationSum(int[] nums, int target) {
        List<int> subset = new List<int>();
        result = new List<List<int>>();
        Subsets(nums, 0, subset, 0, target);
        return result;
    }

    public void Subsets(int[] nums, int index, List<int> subset, int total, int target)
    {
        if(total == target)
        {
            result.Add(new List<int>(subset));
            return;
        }

        if(total > target || index >= nums.Length)
        {
            return;
        } 



        // Include the result.
        subset.Add(nums[index]);
        Subsets(nums, index, subset, total + nums[index], target);

        subset.RemoveAt(subset.Count - 1);
        Subsets(nums, index + 1, subset, total, target);
    }
}
