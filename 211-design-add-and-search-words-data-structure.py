class WordDictionary:
    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        trie = self.trie
        for c in word:
            if c not in trie:
                trie[c] = {}
            trie = trie[c]
        trie['$'] = None

    def search(self, word: str) -> bool:
        tries = [self.trie]
        for c in word:
            delete = []
            for i in range(len(tries)):
                if c == '.':
                    for suffix in tries[i]:
                        if suffix != '$':
                            tries.append(tries[i][suffix])
                    delete.append(i)
                elif c not in tries[i]:
                    delete.append(i)
                else:
                    tries[i] = tries[i][c]

            for i in reversed(delete):
                del tries[i]

            if not tries:
                return False

        return any('$' in trie for trie in tries)
