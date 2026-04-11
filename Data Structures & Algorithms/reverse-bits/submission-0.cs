public class Solution {
    public uint ReverseBits(uint n) {
        uint result = 0;
        int count = 32; // Number of bits in a 32-bit integer
        while (count > 0) {
            result <<= 1; // Shift result to the left by 1 bit
            result |= (n & 1); // Add the least significant bit of n to result
            n >>= 1; // Shift n to the right by 1 bit
            count--; // Decrease the bit count
        }
        
        return result;
    }
}
