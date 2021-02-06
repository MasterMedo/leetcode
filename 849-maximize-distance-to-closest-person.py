from itertools import groupby


class Solution:
    def maxDistToClosest(self, seats: list[int]) -> int:
        distance = seats.index(1)
        seats.reverse()
        distance = max(distance, seats.index(1))
        for seat, group in groupby(seats):
            if seat == 0:
                distance = max(distance, (len(list(group)) + 1) // 2)

        return distance
