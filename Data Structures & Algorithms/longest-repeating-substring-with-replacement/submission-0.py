class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start, result = 0, 0
        s_t = [0] * 26

        for end in range(len(s)):
            s_t[ord(s[end]) - ord('A')] += 1

            while (end - start + 1) - max(s_t) > k:
                s_t[ord(s[start]) - ord('A')] -= 1
                start += 1
            
            result = max(result, end - start + 1)
        
        return result