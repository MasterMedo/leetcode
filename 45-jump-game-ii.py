from math import inf


class Solution:
    def jump(self, arr: list[int]) -> int:
        reachable = [inf] * len(arr)
        reachable[0] = 0
        for i in range(len(reachable)):
            for j in range(i + 1, min(i + arr[i] + 1, len(arr))):
                if reachable[j] > reachable[i]:
                    reachable[j] = reachable[i] + 1

        return reachable[-1]
