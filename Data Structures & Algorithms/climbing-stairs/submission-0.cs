public class Solution {
    public int ClimbStairs(int n) {
        int[] slate = new int[n+1];
        slate[0] = 1;
        slate[1] = 1;

        for(int i = 2; i < n + 1; i++)
        {
            slate[i] = slate[i - 1] + slate[i - 2];
        }

        return slate[n];
    }
}
