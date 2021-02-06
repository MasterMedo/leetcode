class Solution:
    def convertToTitle(self, n: int) -> str:
        ans = []
        while not ans or n != 0:
            n -= 1
            n, m = divmod(n, 26)
            ans.append(chr(m + 65))
        return ''.join(reversed(ans))
