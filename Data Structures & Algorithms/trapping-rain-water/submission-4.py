class Solution:
    def trap(self, height: List[int]) -> int:
        start, end = 0, len(height) - 1
        prev_s, prev_e = 0, 0
        result = 0

        while start < end:
            if height[start] < height[end]:
                if prev_s > height[start]:
                    result += prev_s - height[start]
                else:
                    prev_s = height[start]
                start += 1
            else:
                if prev_e > height[end]:
                    result += prev_e - height[end]
                else:
                    prev_e = height[end]
                end -= 1
        return result