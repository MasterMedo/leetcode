class Solution:
    def lastStoneWeightII(self, stones: list[int]) -> int:
        sum_ = sum(stones)
        sums = {0}
        for stone in stones:
            sums |= {s + stone for s in sums}

        return min(abs(sum_ - s - s) for s in sums)
