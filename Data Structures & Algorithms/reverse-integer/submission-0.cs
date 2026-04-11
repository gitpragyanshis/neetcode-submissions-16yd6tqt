public class Solution {
    public int Reverse(int x) {
        var sign = 1;
        if (x < 0) {
            sign = -1;
            x = -x;
        }

        long result = 0; // Use long to handle overflow
        while (x != 0) {
            result = result * 10 + x % 10;
            x /= 10;
        }

        result *= sign;

        // Check for overflow
        if (result < int.MinValue || result > int.MaxValue) {
            return 0;
        }

        return (int)result;
    }
}
