public class Solution {
    public int Search(int[] nums, int target) {
        return Search(nums, target, 0, nums.Length - 1);
    }

    public int Search(int[] nums, int target, int left, int right) {
        if (left > right) 
        {
            return -1; // Base case: target not found
        }
        var mid = (left + right)/2;

        if(target == nums[mid])
        {
            return mid;
        }
        else if(target < nums[mid])
        {
            return Search(nums, target, left, mid - 1);
        }
        else
        {
            return Search(nums, target, mid + 1, right);
        }  
    }
}
