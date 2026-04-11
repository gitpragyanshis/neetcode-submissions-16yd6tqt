class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0 
        min_profit = prices[0]

        for price in prices:
            profit = price - min_profit
            max_profit = max(profit, max_profit)
            min_profit = min(min_profit, price)
        
        return max_profit