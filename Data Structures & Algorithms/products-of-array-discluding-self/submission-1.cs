public class Solution {
    public int[] ProductExceptSelf(int[] nums) {
        var previous = 1;
        var result = new int[nums.Length];
        result[0] = 1;

        for(int i = 1; i< nums.Length; i++)
        {
            previous *= nums[i - 1];
            result[i] = previous;
        }

        previous = 1;

        for(int i = nums.Length - 2; i >= 0; i--)
        {
            previous *= nums[i + 1];
            result[i] *= previous;
        }

        return result;
    }
}
