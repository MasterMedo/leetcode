class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = dict(zip('IVXLCDM', [1, 5, 10, 50, 100, 500, 1000]))
        n = 0
        for i in range(len(s)-1):
            if (inc := symbols[s[i]]) < symbols[s[i+1]]:
                n -= inc
            else:
                n += inc

        return n + symbols[s[-1]]
