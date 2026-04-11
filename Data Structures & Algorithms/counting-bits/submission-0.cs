public class Solution {
    public int[] CountBits(int n) {
        var r = new int[n+1];
        for(int i = 0; i <= n; i++)
        {
            r[i] = Count(i);
        }

        return r;
    }

    public int Count(int n)
    {
        var result = 0;

        while(n > 0)
        {
            result += n & 1;
            n >>= 1;
        }

        return result;
    }
}
