from collections import defaultdict, Counter


class Solution:
    def maxRepOpt1(self, text: str) -> int:
        max_len = 0
        counter = Counter(text)
        d = defaultdict(int)
        start = 0
        for i, c in enumerate(text):
            d[c] += 1
            if (i - start + 1) - d[c] > 1:
                d[text[start]] -= 1
                start += 1
            else:
                if counter[c] > d[c]:
                    max_len = max(max_len, d[c] + 1)
                else:
                    max_len = max(max_len, d[c])
        return max_len
