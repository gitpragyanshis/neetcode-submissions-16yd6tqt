public class Solution {
    public int MaxSubArray(int[] nums) {
        int max = nums[0];
        int currSum = 0;

        for(int i = 0; i < nums.Length; i++)
        {
            if(currSum < 0)
            {
                currSum = 0;
            }

            currSum += nums[i];
            max = Math.Max(currSum, max); 
        }

        return max;
    }
}
