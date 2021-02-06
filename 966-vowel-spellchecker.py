class Solution:
    def spellchecker(self, words: list[str], queries: list[str]) -> list[str]:
        exact = {}
        changed = {}
        for word in words:
            exact[word] = word
            lower = word.lower()
            changed.setdefault(lower, word)
            voweled = ''.join('.' if c in 'aeiouAEIOU' else c for c in lower)
            changed.setdefault(voweled, word)

        sol = []
        for i, word in enumerate(queries):
            if word in exact:
                sol.append(exact[word])
                continue
            lower = word.lower()
            if lower in changed:
                sol.append(changed[lower])
                continue
            voweled = ''.join('.' if c in 'aeiouAEIOU' else c for c in lower)
            if voweled in changed:
                sol.append(changed[voweled])
                continue
            sol.append('')
        return sol
