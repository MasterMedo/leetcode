class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        a = [None] * len(s)
        for i, c in zip(indices, s):
            a[i] = c

        return ''.join(a)
