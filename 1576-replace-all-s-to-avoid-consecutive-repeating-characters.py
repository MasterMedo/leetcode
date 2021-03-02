class Solution:
    def modifyString(self, s: str) -> str:
        output = ['']
        for i, c in enumerate(s):
            if c == '?':
                next_char = s[i + 1] if i + 1 < len(s) else ''
                prev_char = output[-1]
                output.append(next(char for char in 'abcdef' if char not in (next_char, prev_char)))
            else:
                output.append(c)

        return ''.join(output)
