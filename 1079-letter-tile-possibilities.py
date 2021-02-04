from itertools import permutations


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        return sum(len(set(permutations(tiles, i + 1))) for i in range(len(tiles)))
