public class Solution {
    public int[] TopKFrequent(int[] nums, int k) {
        // Count frequency
        Dictionary<int, int> dict = new Dictionary<int,int>();
        foreach(var num in nums)
        {
            if(!dict.ContainsKey(num))
            {
                dict.Add(num, 1);
            }
            else
            {
                dict[num]++;
            }
        }

        // Initialize temp with enough lists
        var temp = new List<List<int>>(new List<int>[nums.Length + 1]);
        for (int i = 0; i < temp.Count; i++) {
            temp[i] = new List<int>();
        }

        foreach(var key in dict.Keys)
        {
            if (temp[dict[key]] ==  null) temp[dict[key]] =  new List<int>();
            temp[dict[key]].Add(key);
        }

        var result = new List<int>();
        var length = nums.Length;

        while(k > 0 && length > 0)
        {
            var current = temp[length];

            foreach(var element in current)
            {                
                result.Add(element);
                k--;
            }

            length--;
        }

        return result.ToArray();
    }
}
