class Solution:
    def intersect(self, a: list[int], b: list[int]) -> list[int]:
        a.sort()
        b.sort()
        result = []
        i = j = 0
        while i < len(a) and j < len(b):
            left = a[i]
            right = b[j]
            if left == right:
                result.append(left)
                i += 1
                j += 1
            elif left > right:
                j += 1
            else:
                i += 1
        return result
