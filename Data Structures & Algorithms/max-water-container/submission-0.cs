public class Solution {
    public int MaxArea(int[] heights) {
        var result = int.MinValue;
        var start = 0;
        var end = heights.Length - 1;

        while(start < end)
        {
            var area = Math.Min(heights[start], heights[end]) * (end - start);

            result = Math.Max(result, area);

            if(heights[start] <  heights[end])
            {
                start++;
            }
            else
            {
                end--;
            }
        }

        return result;
    }
}
