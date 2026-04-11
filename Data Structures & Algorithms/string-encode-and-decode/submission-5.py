class Solution:
    delimiter = '#'
    def encode(self, strs: List[str]) -> str:
        result = []
        for s in strs:
            result.extend(x for x in str(len(s)))
            result.append(self.delimiter)
            result.extend(s)
        
        r_s = ''.join(str(x) for x in result)
        print(r_s)
        return r_s

    def decode(self, s: str) -> List[str]:
        start = 0
        end = 0
        result = []
        while end < len(s):
            if s[end] == self.delimiter:
                length = int(s[start:end])
                result.append(s[end + 1:end + 1 + length])
                start = end + 1 + length
                end += length + 1
            else:
                end += 1
        return result
