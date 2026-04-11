class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start, profit = prices[0], 0

        for end in range(1, len(prices)):
            curr_p = prices[end] - start
            profit = max(curr_p, profit)
            start = min(start, prices[end])
        
        return profit