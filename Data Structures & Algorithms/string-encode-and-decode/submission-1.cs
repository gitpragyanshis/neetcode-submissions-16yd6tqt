public class Solution {
    private const char delimiter = '#';

    public string Encode(IList<string> strs) {
        var encodedArray = new List<char>();
        foreach(var str in strs)
        {
            foreach(var num in str.Length.ToString())
            {
                encodedArray.Add(num);
            }
            encodedArray.Add(delimiter);
            encodedArray.AddRange(str.ToCharArray());
        }

        Console.WriteLine(new string(encodedArray.ToArray()));

        return new string(encodedArray.ToArray());
    }

    public List<string> Decode(string s) {
        var result = new List<string>();
        int start = 0;
        for(int end = 0; end < s.Length; end++)
        {
            if(s[end] == delimiter)
            {
                var length = Convert.ToInt32(s.Substring(start, end - start));
                var data = s.Substring(end + 1 , length);

                result.Add(data);
                start = end + length + 1;

                end += length + 1;
            }
        }

        return result;
   }
}
