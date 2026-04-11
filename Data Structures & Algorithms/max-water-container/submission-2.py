class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start, end, max_a = 0, len(heights) - 1, 0

        while start < end:
            c_a = min(heights[start], heights[end]) * (end - start)
            print(c_a)
            max_a = max(c_a, max_a)

            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1
        
        return max_a