public class Solution {
    public bool IsAnagram(string s, string t) {
        var map = new Dictionary<char, int>();

        foreach(var c in s)
        {
            if(map.ContainsKey(c))
            {
                map[c]++;
            }
            else
            {
                map.Add(c, 1);
            }
        }

        foreach(var c in t)
        {
            if(map.ContainsKey(c))
            {
                map[c]--;
            }
            else
            {
                return false;
            }
        }

        foreach(var k in map.Keys)
        {
            if(map[k] > 0)
            {
                return false;
            }
        }

        return true;
    }
}
