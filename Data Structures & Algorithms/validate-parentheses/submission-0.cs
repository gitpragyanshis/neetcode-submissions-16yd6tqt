public class Solution {
    public bool IsValid(string s) {
        var stk = new Stack<char>();
        var pair = new Dictionary<char, char>
        {
            {')', '('},
            {'}', '{'},
            {']', '['}
        };

        foreach(var c in s)
        {            
            if(pair.ContainsKey(c))
            {
                if(stk.Any() && stk.Peek() == pair[c])
                {
                    stk.Pop();
                }
                else
                {
                    return false;
                }
            }
            else
            {
                stk.Push(c);
            }
        }
        return !stk.Any();
    }
}
