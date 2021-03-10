class Solution:
    def maxAbsValExpr(self, a: list[int], b: list[int]) -> int:
        arr = [
            [a[i] + b[i] + i for i in range(len(a))],
            [a[i] + b[i] - i for i in range(len(a))],
            [a[i] - b[i] + i for i in range(len(a))],
            [a[i] - b[i] - i for i in range(len(a))],
        ]
        return max(max(i) - min(i) for i in arr)
