from heapq import heappush, heappop


class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        pick_up = []
        drop_off = []
        for n, start, end in trips:
            heappush(pick_up, (start, n))
            heappush(drop_off, (end, n))

        cap = 0
        while drop_off or pick_up:
            t = min(
                pick_up and pick_up[0][0] or float('inf'),
                drop_off and drop_off[0][0] or float('inf')
            )
            while pick_up and pick_up[0][0] <= t:
                cap += heappop(pick_up)[1]

            while drop_off and drop_off[0][0] <= t:
                cap -= heappop(drop_off)[1]

            if cap > capacity:
                return False

        return True
