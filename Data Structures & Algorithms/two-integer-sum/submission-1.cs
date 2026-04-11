public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        var map = new Dictionary<int,int>();
        for(int i=0; i<nums.Length; i++)
        {
            var remaining = target - nums[i];

            if(map.ContainsKey(nums[i]))
            {
                return new[]{map[nums[i]], i};
            }
            if(map.ContainsKey(remaining))
            {
                continue;
            }

            map.Add(remaining, i);
        }

        return null;
    }
}
