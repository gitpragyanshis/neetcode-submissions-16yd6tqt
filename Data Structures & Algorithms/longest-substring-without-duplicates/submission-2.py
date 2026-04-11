class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        start = 0
        res = 0

        for end in range(len(s)):
            while s[end] in char_set:
                char_set.remove(s[start])
                start += 1
            char_set.add(s[end])
            res = max(res, end - start + 1)
        return res