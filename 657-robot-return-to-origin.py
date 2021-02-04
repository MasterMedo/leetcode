class Solution:
    def judgeCircle(self, moves: str) -> bool:
        d = {'U': 1j, 'D': -1j, 'L': -1, 'R': 1}
        return sum(d[move] for move in moves) == 0
