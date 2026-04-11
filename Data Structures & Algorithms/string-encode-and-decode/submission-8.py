class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for s in strs:
            result.append(str(len(s)) + '#' + s)
        return ''.join(result)


    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            length = 0
            while s[i].isdigit():
                length = length * 10 + int(s[i])
                i += 1

            i += 1
            result.append(s[i:i + length])
            i += length

        return result

