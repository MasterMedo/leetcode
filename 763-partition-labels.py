class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        ends = {c: i for i, c in enumerate(s)}
        start = end = 0
        chunks = []
        for i, c in enumerate(s):
            end = max(end, ends[c])
            if i == end:
                chunks.append(end - start + 1)
                start = i + 1

        return chunks
