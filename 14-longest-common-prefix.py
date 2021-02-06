class Solution:
    def longestCommonPrefix(self, words: list[str]) -> str:
        cnt = 0
        for c, *chars in zip(*words):
            if all(char == c for char in chars):
                cnt += 1
            else:
                break

        return words[0][:cnt] if words else ''
