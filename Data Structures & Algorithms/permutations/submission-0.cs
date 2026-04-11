public class Solution {
    public List<List<int>> Permute(int[] nums) {
        List<List<int>> result = new List<List<int>>();
        List<int> slate = new List<int>();
        bool[] used = new bool[nums.Length];
        Backtrack(nums, used, slate, result);
        return result;                 
    }

    private void Backtrack(int[] nums, bool[] used, List<int> slate, List<List<int>> result)
    {
        if(slate.Count == nums.Length)
        {
            result.Add(new List<int>(slate));

            return;
        }

        for(int i = 0; i < nums.Length; i++)
        {
            if(used[i])
            {
                continue;
            }

            used[i] = true;
            slate.Add(nums[i]);
            Backtrack(nums, used, slate, result);
            slate.RemoveAt(slate.Count - 1);
            used[i] = false;
        }
    }
}
