public class Solution {
    public int LongestConsecutive(int[] nums) {
        var set = new HashSet<int>();
        foreach(var num in nums)
        {
            if(set.Contains(num))
            {
                continue;
            }

            set.Add(num);
        }

        var result = 0;
        foreach(var num in nums)
        {
            var tempLength = 0;
            if(!set.Contains(num - 1))
            {
                var tempNum = num;
                while(set.Contains(tempNum))
                {
                    tempNum = tempNum + 1;
                    tempLength++;
                }

                result = Math.Max(result, tempLength);
            }
        }

        return result;
    }
}
