class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_profit = prices[0]
        max_profit = 0

        for price in prices:
            curr_profit = price - min_profit
            min_profit = min(min_profit, price)
            max_profit = max(curr_profit, max_profit)
        
        return max_profit