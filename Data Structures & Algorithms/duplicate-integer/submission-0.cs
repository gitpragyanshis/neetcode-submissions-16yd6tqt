public class Solution {
    public bool hasDuplicate(int[] nums)     {
        Array.Sort(nums);

        for(int index = 1; index < nums.Length; index++)
        {
            if(nums[index] == nums[index-1])
            {
                return true;
            }
        }

        return false;
    }
}
