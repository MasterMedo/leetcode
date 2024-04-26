min2, min3, min5 = [0, 0, 0]
uglies = [1]


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        global min2, min3, min5, uglies
        while n >= len(uglies):
            while uglies[min2] * 2 <= uglies[-1]:
                min2 += 1
            while uglies[min3] * 3 <= uglies[-1]:
                min3 += 1
            while uglies[min5] * 5 <= uglies[-1]:
                min5 += 1

            uglies.append(min(uglies[min5] * 5, uglies[min3] * 3, uglies[min2] * 2))
        return uglies[n - 1]
