from math import inf


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_ = inf
        profit = 0
        for price in prices:
            if min_ > price:
                min_ = price
            else:
                profit = max(profit, price - min_)

        return profit
