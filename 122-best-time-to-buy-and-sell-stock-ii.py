class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        buy = -prices[0]
        for i in range(1, len(prices)):
            profit = max(profit, buy + prices[i])
            buy = max(buy, profit - prices[i])

        return profit
