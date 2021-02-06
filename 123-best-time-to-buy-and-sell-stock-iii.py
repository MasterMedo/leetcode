from math import inf


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy1, sell1 = -inf, 0
        buy2, sell2 = -inf, 0
        for price in prices:
            sell1 = max(sell1, buy1 + price)
            buy1 = max(buy1, -price)
            sell2 = max(sell2, buy2 + price)
            buy2 = max(buy2, sell1 - price)
        return sell2
