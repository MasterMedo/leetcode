class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        d = dict()
        seen = set()
        for n in nums:
            if n in seen:
                continue
            seen.add(n)

            if n - 1 in d and n + 1 in d:
                d[d[n - 1][0]][1] = d[n + 1][1]
                d[d[n + 1][1]][0] = d[n - 1][0]
            elif n - 1 in d:
                d[n] = [d[n - 1][0], n]
                d[d[n - 1][0]][1] = n
            elif n + 1 in d:
                d[n] = [n, d[n + 1][1]]
                d[d[n + 1][1]][0] = n
            else:
                d[n] = [n, n]

        return max(b - a + 1 for a, b in d.values())
