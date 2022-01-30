class Solution:
    def wordsTyping(self, sentence: list[str], rows: int, cols: int) -> int:
        length = len(sentence) + sum(map(len, sentence)) - 1
        row = 1
        col = 0
        i = 0
        seen = [0]
        ans = 0
        while row <= rows:
            if i == 0:
                if row != 1 and col == 1:
                    d, m = divmod(rows, row)
                    return ans * d + seen[m]

                if cols - col >= length:
                    d = (cols - col + 1) // (length + 1)
                    ans += d
                    col += d * (length + 1)

            if len(sentence[i]) + col <= cols:
                col += len(sentence[i]) + 1
                i += 1
                if i >= len(sentence):
                    ans += 1
                    i = 0

            else:
                col = 0
                seen.append(ans)
                row += 1

        return ans
