class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        return [[1 ^ cell for cell in reversed(row)] for row in image]
