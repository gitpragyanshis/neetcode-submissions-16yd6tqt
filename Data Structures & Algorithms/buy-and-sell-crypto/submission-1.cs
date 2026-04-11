public class Solution {
    public int MaxProfit(int[] prices) {
        var profit = 0;
        var minPrice = prices[0];
        for(int i = 0 ; i < prices.Length; i++)
        {
            var currentProfit = prices[i] - minPrice;
            profit = Math.Max(currentProfit, profit);
            minPrice = Math.Min(minPrice, prices[i]);
        }

        return profit;
    }
}
