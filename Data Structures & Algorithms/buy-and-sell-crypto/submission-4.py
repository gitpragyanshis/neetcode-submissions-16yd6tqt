class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_value = prices[0]

        for i in range(1, len(prices)):
            curr_profit = prices[i] - min_value
            max_profit = max(curr_profit, max_profit)
            min_value = min(min_value, prices[i])

        return max_profit
