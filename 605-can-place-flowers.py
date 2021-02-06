from math import ceil


class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        s = 0
        c = 0
        for i in flowerbed:
            if i == 0:
                c += 1
            else:
                c -= 1
                if c > 0:
                    s += ceil(c/2)
                c = -1
        if c:
            s += ceil(c/2)

        return s >= n
