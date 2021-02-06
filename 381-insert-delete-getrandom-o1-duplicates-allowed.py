from collections import defaultdict
import random


class RandomizedCollection:
    def __init__(self):
        self.values = defaultdict(set)
        self.indexes = []
        self.length = 0

    def insert(self, val: int) -> bool:
        self.values[val].add(self.length)
        if len(self.indexes) > self.length:
            self.indexes[self.length] = val
        else:
            self.indexes.append(val)
        self.length += 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.values or not self.values[val]:
            return False

        self.length -= 1
        i = self.values[val].pop()
        if self.length > i:
            self.indexes[i] = self.indexes[self.length]
            self.values[self.indexes[i]].discard(self.length)
            self.values[self.indexes[i]].add(i)
        return True

    def getRandom(self) -> int:
        return self.indexes[random.randint(0, self.length-1)]
