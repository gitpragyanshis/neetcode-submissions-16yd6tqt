public class Solution {
    public int[] DailyTemperatures(int[] temperatures) {
        var stack = new Stack<(int,int)>();
        var result = new int[temperatures.Length];
        for(int i = 0; i< temperatures.Length; i++)
        {
            while(stack.Any() && temperatures[i] > stack.Peek().Item1)
            {
                var data = stack.Pop();
                result[data.Item2] = i - data.Item2;
            }

            stack.Push((temperatures[i], i));
        }

        return result;
    }
}
