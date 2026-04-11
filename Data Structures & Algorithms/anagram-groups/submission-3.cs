public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
        var dict = new Dictionary<string, List<string>>();
        foreach (var str in strs){
            var key = this.GetKey(str);
            if (!dict.ContainsKey(key))
            {
                dict.Add(key, new List<string>());
            }
            dict[key].Add(str);
        }

        return dict.Values.ToList();
        
    }

    private string GetKey(string data) {
        var c = new int[26];
        foreach (var d in data)
        {
            c[d - 'a']++;
        }

        return string.Join('-', c);
    }
}
