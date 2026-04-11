public class Solution {
    List<List<int>> result;
    public List<List<int>> Subsets(int[] nums) {
        List<int> subset = new List<int>();
        result = new List<List<int>>();
        Subsets(nums, 0, subset);
        return result;
    }

    public void Subsets(int[] nums, int index, List<int> subset)
    {
        if(index == nums.Length)
        {
            result.Add(new List<int>(subset));
            return;
        }

        // Include the result.
        subset.Add(nums[index]);
        Subsets(nums, index + 1, subset);

        subset.RemoveAt(subset.Count - 1);
        Subsets(nums, index + 1, subset);
    }
}
