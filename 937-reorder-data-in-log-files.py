class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        def f(log):
            identifier, rest = log.split(' ', maxsplit=1)
            return (0, rest, identifier) if rest[0].isalpha() else (1,)

        return sorted(logs, key=f)
