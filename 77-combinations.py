class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k <= 0:
            return [[]]

        arr = self.combine(n, k - 1)
        result = []
        for i in range(1, n):
            for comb in arr:
                result.append([i, *comb])

        return result
