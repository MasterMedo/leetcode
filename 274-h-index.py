class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort(reverse=True)
        last = 0
        for i, n in enumerate(citations, 1):
            if i <= n:
                last = i
            else:
                break

        return last
