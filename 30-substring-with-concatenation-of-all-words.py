from collections import Counter


class Solution:
    def findSubstring(self, query: str, words: list[str]) -> list[int]:
        n, window = len(words), len(words[0])
        total = n * window
        words = Counter(words)
        seen = {}
        output = []
        index = {}
        for start in range(len(query) - window + 1):
            end = start + window
            word = query[start:end]
            if word in words:
                index[start] = word
                counter, pos = seen.get(start, (Counter(), start))
                counter = counter.copy()
                counter[word] += 1
                while counter[word] > words[word]:
                    counter[index[pos]] -= 1
                    pos += window

                if counter == words:
                    output.append(end - total)

                seen[end] = (counter, pos)
        return output
