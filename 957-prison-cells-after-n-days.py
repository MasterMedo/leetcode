class Solution:
    def prisonAfterNDays(self, cells: list[int], n: int) -> list[int]:
        seen = {tuple(cells): 0}
        index = {0: tuple(cells)}
        for i in range(1, n + 1):
            cells_ = cells.copy()
            for j in range(1, 7):
                cells[j] = 1 if cells_[j - 1] == cells_[j + 1] else 0

            cells[0] = cells[7] = 0
            cells_ = tuple(cells)
            if cells_ not in seen:
                seen[cells_] = i
                index[i] = cells_
            else:
                return index[(n - seen[cells_]) % (i - seen[cells_]) + seen[cells_]]

        return cells
