public class Solution {
    public List<List<int>> SubsetsWithDup(int[] nums) {
        List<List<int>> res = new List<List<int>>();
        Array.Sort(nums);
        Backtrack(0,nums, new List<int>(), res);
        return res;
    }

    public void Backtrack(int start, int[] nums, List<int> slate, List<List<int>> result)
    {
        result.Add(new List<int>(slate));

        for(int i = start; i < nums.Length; i++)
        {
            if(i > start && nums[i] == nums[i -1])
            {
                continue;
            }

            slate.Add(nums[i]);
            Backtrack(i + 1, nums, slate, result);
            slate.Remove(nums[i]);
        }
    }
}
