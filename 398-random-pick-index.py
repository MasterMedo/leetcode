import random
from collections import defaultdict


class Solution:
    def __init__(self, arr: list[int]):
        self.d = defaultdict(list)
        for i, n in enumerate(arr):
            self.d[n].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.d[target])
