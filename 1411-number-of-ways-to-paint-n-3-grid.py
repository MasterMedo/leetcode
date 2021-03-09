class Solution:
    def numOfWays(self, n: int) -> int:
        ways = [(0, 1, 0), (1, 0, 1), (2, 0, 1),
                (0, 1, 2), (1, 0, 2), (2, 0, 2),
                (0, 2, 0), (1, 2, 0), (2, 1, 0),
                (0, 2, 1), (1, 2, 1), (2, 1, 2)]

        matching = {way: [w for w in ways if all(w[i] != way[i] for i in range(3))] for way in ways}
        d = {way: 1 for way in ways}
        while n > 1:
            d_ = d.copy()
            for way in ways:
                d_[way] = sum(d[w] for w in matching[way]) % (10 ** 9 + 7)
            n -= 1
            d = d_

        return sum(d.values()) % (10 ** 9 + 7)
