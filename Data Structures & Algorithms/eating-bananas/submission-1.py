class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles) + 1

        while left < right:
            mid = (left + right) // 2

            curr = sum((v + mid - 1) // mid for v in piles)

            if curr <= h:
                right = mid
            else:
                left = mid + 1
        
        return left