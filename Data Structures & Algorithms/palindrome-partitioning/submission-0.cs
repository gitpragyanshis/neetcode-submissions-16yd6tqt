public class Solution {
    public List<List<string>> Partition(string s) {
        var res = new List<List<string>>();        
        Backtrack(0, s, new List<string>(), res);
        return res;
    }

    public void Backtrack(int start, string s, List<string> slate, List<List<string>> result)
    {
        if (start >= s.Length) {
            result.Add(new List<string>(slate));
            return;
        }

        for(int i = start; i < s.Length; i++)
        {
            if (IsPali(s, start, i)) {
                slate.Add(s.Substring(start, i - start + 1));
                Backtrack(i + 1, s, slate, result);
                slate.RemoveAt(slate.Count - 1); // Remove the last element
            }
        }
    }

    private bool IsPali(string s, int l, int r) {
        while (l < r) {
            if (s[l] != s[r]) {
                return false;
            }
            l++;
            r--;
        }
        return true;
    }
}
