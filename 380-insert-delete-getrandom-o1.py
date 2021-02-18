import random


class RandomizedSet:
    def __init__(self):
        self.arr = []
        self.index = {}

    def insert(self, val: int) -> bool:
        contains = val in self.index
        if not contains:
            self.index[val] = len(self.arr)
            self.arr.append(val)
        return not contains

    def remove(self, val: int) -> bool:
        contains = val in self.index
        if contains:
            if len(self.arr) == 1:
                self.arr = []
                self.index = {}
            else:
                i = self.index.pop(val)
                last = self.arr.pop()
                if val != last:
                    self.arr[i] = last
                    self.index[last] = i
        return contains

    def getRandom(self) -> int:
        return random.choice(self.arr)
