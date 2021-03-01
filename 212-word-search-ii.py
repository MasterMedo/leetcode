class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        def dfs(r, c, trie):
            for dr, dc in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(board) \
                        and 0 <= nc < len(board[0]) \
                        and not seen[nr][nc] \
                        and board[nr][nc] in trie:

                    seen[nr][nc] = True
                    if '*' in trie[board[nr][nc]]:
                        output.append(trie[board[nr][nc]]['*'])
                        del trie[board[nr][nc]]['*']

                    dfs(nr, nc, trie[board[nr][nc]])
                    seen[nr][nc] = False

        trie = {}
        for word in words:
            cur = trie
            for c in word:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            cur['*'] = word

        output = []
        seen = [[False]*len(board[0]) for _ in range(len(board))]
        for r, row in enumerate(board):
            for c, char in enumerate(row):
                if char in trie:
                    seen[r][c] = True
                    if '*' in trie[char]:
                        del trie[char]['*']
                        output.append(char)

                    dfs(r, c, trie[char])
                    seen[r][c] = False

        return output
