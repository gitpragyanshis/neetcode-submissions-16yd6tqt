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
        result.Add(new List<int>(subset));

        for(int i = index; i < nums.Length; i++)
        {
            subset.Add(nums[i]);            
            Subsets(nums, i + 1, subset);
            subset.RemoveAt(subset.Count - 1);
        }
    }
}
