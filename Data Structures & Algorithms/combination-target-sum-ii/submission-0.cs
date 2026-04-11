public class Solution {
    public List<List<int>> CombinationSum2(int[] candidates, int target) {
        var res = new List<List<int>>();
        Array.Sort(candidates);
        Backtrack(0, target, candidates, new List<int>(), res);
        return res;
    }

    public void Backtrack(int start, int target, int[] nums, List<int> slate, List<List<int>> result)
    {
        if(target == 0)
        {
            result.Add(new List<int>(slate));
        }

        if(target < 0)
        {
            return;
        }

        for(int i = start; i < nums.Length; i++)
        {
            if(i > start && nums[i] == nums[i -1])
            {
                continue;
            }

            slate.Add(nums[i]);
            Backtrack(i+ 1, target - nums[i], nums, slate, result);
            slate.Remove(nums[i]);
        }
    }
}
