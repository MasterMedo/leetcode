class ProductOfNumbers:
    def __init__(self):
        self.arr = []

    def add(self, n: int) -> None:
        if n == 0:
            self.arr = []
        elif not self.arr:
            self.arr.append(n)
        else:
            self.arr.append(self.arr[-1] * n)

    def getProduct(self, k: int) -> int:
        if len(self.arr) < k:
            return 0
        if len(self.arr) == k:
            return self.arr[-1]

        return self.arr[-1] // self.arr[-k - 1]
