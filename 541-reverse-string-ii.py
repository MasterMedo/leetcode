class Solution:
    def reverseStr(self, s: str, n: int) -> str:
        r = []
        for i in range(0, len(s), 2*n):
            j = min(i + n, len(s))
            k = min(i + 2*n, len(s))
            r.extend(reversed(s[i:j]))
            r.extend(s[j:k])

        return ''.join(r)
