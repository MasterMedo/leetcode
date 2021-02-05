from collections import deque


class StockSpanner:
    def __init__(self):
        self.prices = deque()

    def next(self, price: int) -> int:
        span = 1
        while self.prices:
            prev_price, prev_span = self.prices[-1]
            if prev_price <= price:
                span += prev_span
                self.prices.pop()
            else:
                break

        self.prices.append([price, span])
        return span
