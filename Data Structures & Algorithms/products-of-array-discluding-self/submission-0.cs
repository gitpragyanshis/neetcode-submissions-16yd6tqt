public class Solution {
    public int[] ProductExceptSelf(int[] nums) {
        var result = new int[nums.Length];
        result[0] = 1;

        var prefix = 1;
        for(int i = 1; i < nums.Length; i++)
        {
            prefix *= nums[i - 1];            
            result[i] = prefix;
        }

        prefix = 1;
        for (int i = nums.Length - 2; i >= 0; i--) {
            prefix *= nums[i + 1];
            result[i] *= prefix;
        }

        return result;
    }
}
