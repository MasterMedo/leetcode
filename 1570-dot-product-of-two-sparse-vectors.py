class SparseVector:
    def __init__(self, nums: list[int]):
        self.vals = {i: n for i, n in enumerate(nums) if n}

    def dotProduct(self, vec: "SparseVector") -> int:
        return sum(vec.vals[i] * self.vals[i] for i in vec.vals if i in self.vals)
