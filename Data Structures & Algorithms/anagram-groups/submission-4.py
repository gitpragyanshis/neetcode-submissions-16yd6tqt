class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d: dict[str, List[str]] = defaultdict(list)

        for s in strs:
            k = self.getKey(s)

            d[k].append(s)

        return [v for k, v in d.items()]

    def getKey(self, s: str) -> str:
        arr = [0] * 26

        for c in s:
            arr[ord(c) - ord('a')] += 1

        return '-'.join([str(v) for v in arr])