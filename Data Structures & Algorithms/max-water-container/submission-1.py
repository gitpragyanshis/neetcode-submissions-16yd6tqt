class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start, end, max_a = 0, len(heights) - 1, 0

        while start < end:
            curr_area = min(heights[start], heights[end]) * (end - start)
            max_a = max(max_a, curr_area)

            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1
        return max_a