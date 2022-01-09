class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * size
        self.bit_mask = 1  # largest power of 2 smaller than (size - 1)
        while self.bit_mask * 2 < size - 1:
            self.bit_mask *= 2

    def add(self, index, amount):
        while index < self.size:
            self.tree[index] += amount
            index += index & -index

    def get_index_of_sum(self, sum_) -> int:
        ans_i = 0
        bit_mask = self.bit_mask
        while bit_mask != 0:
            fenwick_i = ans_i + bit_mask
            bit_mask //= 2
            if fenwick_i < self.size and sum_ > self.tree[fenwick_i]:
                ans_i = fenwick_i
                sum_ -= self.tree[fenwick_i]

        return ans_i if ans_i != self.size - 1 else ans_i - 1


class Solution:
    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:
        people.sort(key=lambda p: (p[0], -p[1]))
        ans = [None] * len(people)
        fenwick_tree = FenwickTree(len(people) + 1)

        for i in range(2, len(people) + 1):
            fenwick_tree.add(i, 1)

        for height, taller_in_front in people:
            i = fenwick_tree.get_index_of_sum(taller_in_front)
            ans[i] = [height, taller_in_front]
            fenwick_tree.add(i + 1, -1)

        return ans
