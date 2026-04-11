class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {}

        for i in nums:
            if i in count_map:
                count_map[i] += 1
            else:
                count_map[i] = 1
        temp = [[] for _ in range(len(nums) + 1)]
        print(temp)
        for key, value in count_map.items():            
            temp[value].append(key)
            
        length = len(temp) - 1
        result = []
        while length >= 0 and k > 0:
            if temp[length]:
                result.extend(temp[length])
                k -= len(temp[length])
            length -= 1        
        
        return result





