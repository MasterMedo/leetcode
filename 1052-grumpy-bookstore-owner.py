class Solution:
    def maxSatisfied(self, customers: list[int], grumpy: list[int], X: int) -> int:
        m = r = c = 0
        for i, e in enumerate(customers):
            if i - X >= 0 and grumpy[i - X] == 1:
                c -= customers[i - X]
            if grumpy[i] == 0:
                r += e
            else:
                c += e
            m = max(m, c)

        return r + m
