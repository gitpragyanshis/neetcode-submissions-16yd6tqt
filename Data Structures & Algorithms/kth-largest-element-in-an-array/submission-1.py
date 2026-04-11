class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        container = []

        for num in nums:
            heapq.heappush(container, num)

            if len(container) > k:
                heapq.heappop(container)
        
        return heapq.heappop(container)