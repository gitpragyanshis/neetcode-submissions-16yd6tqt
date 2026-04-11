"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        result = 0
        heap = []
        intervals.sort(key=lambda x: x.start)

        for interval in intervals:
            if not heap:
                heapq.heappush(heap, interval.end)
            else:
                if interval.start >= heap[0]:
                    heapq.heappop(heap)
                heapq.heappush(heap, interval.end)
        return len(heap)


