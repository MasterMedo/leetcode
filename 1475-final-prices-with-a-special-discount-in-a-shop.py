from collections import deque


class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        discounted = prices.copy()
        stack = deque()
        for j in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[j]:
                discounted[stack.pop()] -= prices[j]

            stack.append(j)
        return discounted
