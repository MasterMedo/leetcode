class Solution:
    def countBits(self, n: int) -> List[int]:
        def bitcount(n):
            cnt = 0
            while n:
                n &= n - 1
                cnt += 1
            return cnt

        return [bitcount(i) for i in range(n + 1)]
