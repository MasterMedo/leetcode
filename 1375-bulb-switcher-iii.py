from heapq import heappush, heappop


class Solution:
    def numTimesAllBlue(self, light: list[int]) -> int:
        on = []
        blue = 0
        moments = 0
        for switch in light:
            if switch - 1 == blue:
                blue += 1
                while on and on[0] == blue + 1:
                    blue = heappop(on)
            else:
                heappush(on, switch)

            if not on:
                moments += 1

        return moments
