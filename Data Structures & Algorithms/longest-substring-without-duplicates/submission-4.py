class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = set()
        result = 0
        start = 0

        for end in range(len(s)):
            while s[end] in st:
                st.remove(s[start])
                start += 1
            st.add(s[end])
            result = max(result, end - start + 1)
        return result