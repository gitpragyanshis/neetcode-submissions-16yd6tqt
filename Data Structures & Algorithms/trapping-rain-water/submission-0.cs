public class Solution {
    public int Trap(int[] height) {
        var result = 0;
        var left = 0;
        var right = height.Length - 1;
        var leftMin = 0;
        var rightMin = 0;


        while (left < right) 
        {
            if (height[left] < height[right]) {
                leftMin = Math.Max(leftMin, height[left]);
                var tempResult = leftMin - height[left];
                result += tempResult > 0 ? tempResult : 0;
                left++;
            } else {
                rightMin = Math.Max(rightMin, height[right]);
                var tempResult = rightMin - height[right];
                result += tempResult > 0 ? tempResult : 0;
                right--;
            }
        }

        return result;
    }
}
