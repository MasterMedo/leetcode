from collections import defaultdict


class Solution:
    def numIdenticalPairs(self, numbers: list[int]) -> int:
        pairs = 0
        occurrences = defaultdict(int)
        for n in numbers:
            pairs += occurrences[n]
            occurrences[n] += 1

        return pairs
