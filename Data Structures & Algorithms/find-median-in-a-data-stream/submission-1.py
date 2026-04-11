class MedianFinder:

    def __init__(self):
        self.left_max = []
        self.right_min = []
        

    def addNum(self, num: int) -> None:
        if not self.right_min or num >= self.right_min[0]:
            heapq.heappush(self.right_min, num)
        else:
            heapq.heappush_max(self.left_max, num)

        if len(self.right_min) > len(self.left_max) + 1:
            heapq.heappush_max(self.left_max, heapq.heappop(self.right_min))
        elif len(self.left_max) > len(self.right_min):
            heapq.heappush(self.right_min, heapq.heappop_max(self.left_max))
        

    def findMedian(self) -> float:
        if len(self.left_max) == len(self.right_min):
            return (self.left_max[0] + self.right_min[0]) / 2
        else:
            return float(self.right_min[0])
        