class Solution:
    def numSpecialEquivGroups(self, arr: list[str]) -> int:
        groups = set()
        for word in arr:
            even, odd = tuple(sorted(word[::2])), tuple(sorted(word[1::2]))
            groups.add((even, odd))

        return len(groups)
