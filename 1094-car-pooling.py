class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        times = []
        for n, start, end in trips:
            times.append((start, n))
            times.append((end, -n))

        times.sort()
        cap = 0
        for _, n in times:
            cap += n
            if cap > capacity:
                return False

        return True
