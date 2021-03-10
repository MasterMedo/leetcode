class Solution:
    def shortestCommonSupersequence(self, a: str, b: str) -> str:
        if not a:
            return b

        if not b:
            return a

        if len(a) > len(b):
            a, b = b, a

        dp = [''] * (len(a) + 1)
        for j, c2 in enumerate(b):
            new_dp = dp[:]
            for i, c1 in enumerate(a):
                if c1 == c2:
                    new_dp[i + 1] = dp[i] + c1

                elif len(new_dp[i]) > len(dp[i]):
                    new_dp[i + 1] = new_dp[i]

            dp = new_dp

        ans = ''
        i = j = 0
        for c in dp[-1]:
            while a[i] != c:
                ans += a[i]
                i += 1

            while b[j] != c:
                ans += b[j]
                j += 1

            ans += c
            i += 1
            j += 1

        return ans + a[i:] + b[j:]
