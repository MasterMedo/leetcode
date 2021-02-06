from math import inf


class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        if not prices or k <= 0:
            return 0

        k = min(k, len(prices))

        buys = [-inf]*k
        sells = [0]*k
        for price in prices:
            for i in range(k):
                sell = sells[i-1] if i != 0 else 0
                buys[i] = max(buys[i], sell - price)
                sells[i] = max(sells[i], buys[i] + price)

        return sells[-1]
