public class Solution {
    public int LengthOfLongestSubstring(string s) {
        HashSet<char> set = new HashSet<char>();
        int startIndex = 0;
        int result = 0;
        for(int i = 0; i < s.Length; i++)
        {
            while(set.Contains(s[i]))
            {
                set.Remove(s[startIndex]);
                startIndex++;
            }

            set.Add(s[i]);
            result = Math.Max(result, i - startIndex + 1);
        }

        return result;
    }
}
