class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start, end, area = 0, len(heights) - 1, 0

        while start < end:
            curr_area = min(heights[start], heights[end]) * (end - start)
            area = max(curr_area, area)

            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1
        return  area