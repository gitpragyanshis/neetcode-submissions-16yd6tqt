class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.convert(s) == self.convert(t)

    def convert(self, s: str) -> str:
        c_arr = [0] * 26
        for c in s:
            c_arr[ord(c) - ord('a')] = c_arr[ord(c) - ord('a')] + 1
        return '-'.join(str(x) for x in c_arr)
        