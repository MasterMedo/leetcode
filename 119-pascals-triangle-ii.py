from math import factorial as f


class Solution:
    def getRow(self, n: int) -> List[int]:
        return [f(n) // (f(k) * f(n - k)) for k in range(n + 1)]
