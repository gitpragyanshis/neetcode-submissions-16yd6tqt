class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for s in strs:
            result.append(f'{str(len(s))}#{s}')
        
        return ''.join(result)


    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        w_l = 0

        while i < len(s):
            if s[i].isdigit():
                w_l = w_l * 10 + int(s[i])
                i += 1
            else:
                i += 1
                result.append(s[i : i + w_l])
                i += w_l
                w_l = 0

        return result
