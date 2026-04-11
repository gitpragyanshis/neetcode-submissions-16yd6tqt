public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
        var map = new Dictionary<string, List<string>>();

        foreach(var str in strs)
        {
            int[] set = new int[26];
            foreach(var c in str)
            {
                set[c - 'a']++;
            }

            var key = string.Join(",", set);

            if(map.ContainsKey(key))
            {
                map[key].Add(str);
            }
            else
            {
                map[key] = new List<string>(){str};
            }
        }

        return map.Select(e=> e.Value).ToList();
    }
}
