class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        index = 0
        for i, c in enumerate(reversed(columnTitle)):
            index += (ord(c) - 64) * pow(26, i)

        return index
