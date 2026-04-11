class Solution:
    def countBits(self, n: int) -> List[int]:
        def countBit(d: int) -> int:
            result = 0
            while d > 0:
                result += (d & 1)
                d >>= 1
            return result
        r = []
        for i in range(n + 1):
            r.append(countBit(i))
        
        return r