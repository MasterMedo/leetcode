from heapq import heappop, heappush
from collections import Counter


class Solution:
    def leastInterval(self, tasks: list[str], k: int) -> int:
        counter = Counter(tasks)
        orders = []
        for task, count in counter.items():
            heappush(orders, (-count, task))

        t = 0
        cooldown = []
        while counter:
            if cooldown and cooldown[0][0] <= t:
                _, task = heappop(cooldown)
                heappush(orders, (-counter[task], task))

            if orders:
                _, task = heappop(orders)
                counter[task] -= 1
                if counter[task] == 0:
                    del counter[task]
                else:
                    heappush(cooldown, (t + k + 1, task))

                t += 1
            else:
                t, _ = cooldown[0]

        return t
