class Fancy:
    def __init__(self, mod=1000000007):
        self.mod = mod
        self.add = 0
        self.mul = 1
        self.arr = []

    def append(self, val: int) -> None:
        self.arr.append((val - self.add) * pow(self.mul, -1, self.mod))

    def addAll(self, inc: int) -> None:
        self.add += inc

    def multAll(self, m: int) -> None:
        self.add = self.add * m % self.mod
        self.mul = self.mul * m % self.mod

    def getIndex(self, i: int) -> int:
        if 0 <= i < len(self.arr):
            return (self.arr[i] * self.mul + self.add) % self.mod
        return -1
