class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        line = [words[0]]
        length = len(words[0])
        for word_i in range(1, len(words)):
            word = words[word_i]
            if length + 1 + len(word) <= maxWidth:
                length += 1 + len(word)
                line.append(word)
            else:
                spaces = len(line) - 1
                space_left = maxWidth - length + spaces
                if spaces == 0:
                    lines.append("".join(line) + " " * (space_left))
                else:
                    size, amount_extra = divmod(space_left, spaces)
                    elements = []
                    for i in range(len(line) - 1):
                        elements.append(line[i])
                        s = size + 1 if amount_extra > i else size
                        elements.append(" " * s)
                    elements.append(line[-1])
                    lines.append("".join(elements))
                line = [word]
                length = len(word)
        if line:
            lines.append(" ".join(line) + " " * (maxWidth - length))
        return lines
