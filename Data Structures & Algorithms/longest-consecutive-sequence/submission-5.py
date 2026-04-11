import heapq
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        heap = nums.copy()
        heapq.heapify(heap)

        t_result = 0
        result = 0
        prev = None

        while heap:
            curr = heapq.heappop(heap)

            if prev is None:
                t_result = 1
            elif curr == prev:
                continue
            elif curr - prev == 1:
                t_result += 1
            else:
                t_result = 1

            result = max(result, t_result)
            prev = curr


        return result 



            

