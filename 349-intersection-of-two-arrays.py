class Solution:
    def intersection(self, a: list[int], b: list[int]) -> list[int]:
        a, b = set(a), set(b)
        if len(a) > len(b):
            a, b = b, a

        return [x for x in a if x in b]
