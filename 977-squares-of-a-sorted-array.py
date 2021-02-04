from heapq import merge
from bisect import bisect_left


class Solution:
    def sortedSquares(self, arr: list[int]) -> list[int]:
        zero = bisect_left(arr, 0)
        return merge((arr[i]**2 for i in range(zero-1, -1, -1)),
                     (arr[i]**2 for i in range(zero, len(arr))))
