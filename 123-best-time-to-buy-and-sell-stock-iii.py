class Solution:
    def maxProfit(self, prices) -> int:
        profit1 = profit2 = 0
        buy1 = buy2 = prices[0]

        for price in prices:
            if price < buy1:
                buy1 = price

            if price - buy1 > profit1:
                profit1 = price - buy1

            if price - profit1 < buy2:
                buy2 = price - profit1

            if price - buy2 > profit2:
                profit2 = price - buy2

        return profit2
