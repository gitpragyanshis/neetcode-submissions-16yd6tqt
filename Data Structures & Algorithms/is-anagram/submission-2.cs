public class Solution {
    public bool IsAnagram(string s, string t) {
        var set = new char[26];

        foreach(var c in s)
        {
            set[c - 'a']++;
        }

        foreach(var c in t)
        {
            var index = c - 'a';

            if(set[index] > 0)
            {
                set[index]--;
            }
            else
            {
                return false;
            }
        }

        return !set.Any(e=> e > 0);            
    }
}
