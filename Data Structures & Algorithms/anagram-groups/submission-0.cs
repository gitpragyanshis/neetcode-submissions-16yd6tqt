public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
        var dict = new Dictionary<string, List<string>>();
        foreach(var s in strs)
        {
            var cCount = new int[26];

            foreach(var c in s)
            {
                cCount[c - 'a']++;
            }

            var key = string.Join(',', cCount);
            if(!dict.ContainsKey(key))
            {
                dict.Add(key, new List<string>{s});
            }  
            else
            {
                dict[key].Add(s);
            }          
        }

        return dict.Values.ToList();
    }
}
