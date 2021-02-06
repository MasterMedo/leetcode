class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0

        buy = -prices[0]
        sell = 0
        cooldown = 0
        profit = 0
        for i in range(1, len(prices)):
            price = prices[i]
            prev_buy = buy
            prev_sell = sell

            buy = max(buy, cooldown - price)
            sell = prev_buy + price
            cooldown = max(cooldown, prev_sell)
            profit = max(cooldown, sell)

        return profit
