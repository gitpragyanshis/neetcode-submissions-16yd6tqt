public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        var set = new Dictionary<int,int>();

        for(int i = 0; i< nums.Length; i++)
        {
            if(set.Keys.Contains(nums[i]))
            {
                return new int[] {set[nums[i]], i};
            }
            else
            {
                set.Add(target - nums[i], i);
            }
        }

        return null;
    }
}
