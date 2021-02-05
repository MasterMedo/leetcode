class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        profit = 0
        buy = -prices[0]
        for i in range(1, len(prices)):
            profit = max(profit, buy + prices[i] - fee)
            buy = max(buy, profit - prices[i])

        return profit
