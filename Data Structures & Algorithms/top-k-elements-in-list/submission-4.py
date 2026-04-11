class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)

        for num in nums:
            d[num] += 1
        
        temp_result = [[] for _ in range(len(nums) + 1)]

        for key, value in d.items():
            temp_result[value].append(key)
        
        result = []
        for i in range(len(temp_result) - 1, -1, -1):
            if temp_result[i]:
                while temp_result[i]:
                    result.append(temp_result[i].pop())
                    k -= 1

                    if k == 0:
                        return result

        return None