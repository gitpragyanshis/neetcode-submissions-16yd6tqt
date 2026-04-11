class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        for w in strs:
            k = self.get_Key(w)
            if k in m:
                m[k].append(w)
            else:
                m[k] = [w]
        return m.values()
    def get_Key(self, s: str) -> str:
        c_a = [0] * 26

        for c in s:
            c_a[ord(c) - ord('a')] = c_a[ord(c) - ord('a')] + 1
        
        return '-'.join(str(i) for i in c_a)