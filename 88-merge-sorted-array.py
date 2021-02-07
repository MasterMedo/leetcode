class Solution:
    def merge(self, a: list[int], m: int, b: list[int], n: int) -> None:
        i = m + n - 1
        n -= 1
        m -= 1
        while i >= 0:
            if n < 0 or (m >= 0 and a[m] > b[n]):
                a[i] = a[m]
                m -= 1
            else:
                a[i] = b[n]
                n -= 1
            i -= 1
