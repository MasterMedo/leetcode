class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        return set.difference(*reversed(list(map(set, zip(*paths))))).pop()
