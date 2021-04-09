class Solution:
    def findReplaceString(self, string: str, indexes: list[int], sources: list[str], targets: list[str]) -> str:
        s = ''
        i = 0
        for index, source, target in sorted(zip(indexes, sources, targets)):
            while i < index:
                s += string[i]
                i += 1
            if string[index:index + len(source)] == source:
                s += target
                i += len(source)

        return s + string[i:]
