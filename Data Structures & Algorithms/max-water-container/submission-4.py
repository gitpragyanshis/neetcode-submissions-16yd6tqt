class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start, end = 0, len(heights) - 1
        result = 0

        while start < end:
            curr = min(heights[start], heights[end]) * (end - start)
            result = max(curr, result)

            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1

        return result
