class Solution:
    def longestPalindrome(self, s: str) -> str:
        expanded = '|'.join(f'^{s}$')
        seen = [0] * len(expanded)
        center = right = 0
        for i in range(1, len(expanded) - 1):
            if right > i:
                seen[i] = min(right - i, seen[2 * center - i])

            while expanded[i + 1 + seen[i]] == expanded[i - 1 - seen[i]]:
                seen[i] += 1

            if i + seen[i] > right:
                center, right = i, i + seen[i]

        length, center = max((n, i) for i, n in enumerate(seen))
        return s[(center - length) // 2:(center + length) // 2]
