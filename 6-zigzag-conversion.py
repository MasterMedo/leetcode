class Solution:
    def convert(self, s: str, rows: int) -> str:
        lists = [[] for _ in range(rows)]
        i = 0
        d = 1
        for c in s:
            lists[i].append(c)
            if rows != 1:
                i += d
            if i <= 0:
                d = 1
            if i >= rows - 1:
                d = -1

        return ''.join(''.join(lists[i]) for i in range(rows))
