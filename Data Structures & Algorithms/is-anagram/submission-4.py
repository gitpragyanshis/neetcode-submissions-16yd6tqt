class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_key = self.getKey(t)
        t_key = self.getKey(s)

        return s_key == t_key
    
    def getKey(self, s: str) -> str:
        arr = [0] * 26

        for c in s:
            arr[ord(c) - ord('a')] += 1
        
        print(arr)
        return ''.join([str(v) for v in arr])
        
