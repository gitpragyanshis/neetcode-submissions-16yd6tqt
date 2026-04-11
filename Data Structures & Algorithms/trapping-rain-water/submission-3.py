class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l_m, r_m, start, end = 0, 0, 0, len(height) - 1
        total = 0

        while start < end:
            if height[start] < height[end]:
                curr = l_m - height[start]
                if curr >= 0:
                    total += curr
                l_m = max(l_m, height[start])
                start += 1
            else:
                curr = r_m - height[end]
                if curr >= 0:
                    total += curr
                r_m = max(r_m, height[end])
                end -= 1
        
        return total


            
            
