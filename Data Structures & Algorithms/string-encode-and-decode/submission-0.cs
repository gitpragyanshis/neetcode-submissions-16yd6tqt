public class Solution {
    private const char delimiter = '#';

    public string Encode(IList<string> strs) {
        var result = new List<char>();
        foreach(var s in strs)
        {
            result.AddRange(s.Length.ToString());
            result.Add(delimiter);
            result.AddRange(s.ToCharArray());
        }

        return new string(result.ToArray());
    }

    public List<string> Decode(string s) {
        var result = new List<string>();
        var start = 0;
        for (int i = 0; i < s.Length; i++) {                        
            if (s[i] == delimiter) {                
                var lengthString = s.Substring(start, i - start);
                var length = Convert.ToInt32(lengthString);
                var startIndex = i + 1;

                result.Add(s.Substring(startIndex, length));

                start = startIndex + length;
                i = start - 1; // Adjust the loop index to continue after the current string
            }                  
        }
        return result; 
   }
}
