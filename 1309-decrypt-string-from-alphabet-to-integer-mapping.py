class Solution:
    def freqAlphabets(self, s: str) -> str:
        skips = 0
        current = ''
        result = []
        for c in reversed(s):
            if c == '#':
                skips = 1
                continue

            current = c + current
            if skips > 0:
                skips -= 1
            else:
                result.append(chr(int(current) + 96))
                current = ''

        return ''.join(reversed(result))
