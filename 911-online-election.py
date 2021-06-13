from bisect import bisect
from collections import defaultdict


class TopVotedCandidate:
    def __init__(self, persons: list[int], times: list[int]):
        self.leaders = [persons[0]]
        self.times = [times[0]]
        person = defaultdict(int)
        person[persons[0]] += 1
        for p, t in zip(persons[1:], times[1:]):
            person[p] += 1
            if p != self.leaders[-1] and person[p] >= person[self.leaders[-1]]:
                self.leaders.append(p)
                self.times.append(t)

    def q(self, t: int) -> int:
        return self.leaders[min(max(bisect(self.times, t), 1), len(self.leaders)) - 1]
