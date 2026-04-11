class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for i,v in enumerate(nums):
            if v in s:
                return [s[v], i]
            else:
                s[target - v] = i
        return None