class Solution:
    def removeComments(self, source: list[str]) -> list[str]:
        output = []
        comment = False
        for line in source:
            last_char = ''
            if not comment:
                line_chars = []
            for c in line:
                if comment:
                    if last_char == '*' and c == '/':
                        comment = False
                        last_char = ''
                    else:
                        last_char = c
                else:
                    if last_char == '/' and c == '*':
                        comment = True

                    elif last_char == '/' and c == '/':
                        last_char = ''
                        break

                    else:
                        line_chars.append(last_char)
                        last_char = c
            else:
                if not comment:
                    line_chars.append(last_char)

            if not comment:
                line = ''.join(line_chars)
                if line:
                    output.append(line)
        return output
