class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        r = []

        for i in range(len(nums)):
            if nums[i] in m:
                m[nums[i]] += 1
            else:
                m[nums[i]] = 1
        res = [[] for i in range(len(nums) + 1)]

        for key, value in m.items():
            res[value].append(key)
        
        for i in range(len(res) - 1, -1, -1):
            for j in range(len(res[i])):
                r.append(res[i][j])
                k -= 1

                if k == 0:
                    return r
        return None






