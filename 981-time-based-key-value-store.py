from collections import defaultdict
from bisect import bisect


class TimeMap:
    def __init__(self):
        self.dictionary = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dictionary[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        i = bisect(self.dictionary[key], (timestamp, '\xFF'))
        return self.dictionary[key][i - 1][1] if i != 0 else ''
