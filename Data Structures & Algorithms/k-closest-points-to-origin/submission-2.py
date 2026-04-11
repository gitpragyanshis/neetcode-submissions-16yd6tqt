class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = [(x ** 2 + y ** 2, [x, y]) for x, y in points]
        heapq.heapify(distance)
        result = []

        while k:
            _, point = heapq.heappop(distance)
            result.append(point)
            k -= 1
        
        return result
