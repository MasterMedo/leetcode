from heapq import nlargest


class Solution:
    def maxProduct(self, numbers: list[int]) -> int:
        def product(a, b):
            return (a - 1) * (b - 1)

        return product(*nlargest(2, numbers))
