class Solution:
    def intToRoman(self, n: int) -> str:
        vals = [
            (1000, 'M', 2),
            (500, 'D', 2),
            (100, 'C', 4),
            (50, 'L', 4),
            (10, 'X', 6),
            (5, 'V', 6),
            (1, 'I', 7),
            (0, '', 7)
        ]
        roman = []
        for i in range(len(vals)-1):
            v1, r1, j = vals[i]
            v2, r2, _ = vals[j]
            while n >= v1:
                roman.append(r1)
                n -= v1

            if n >= v1 - v2:
                roman.extend([r2, r1])
                n -= v1 - v2
        return ''.join(roman)
