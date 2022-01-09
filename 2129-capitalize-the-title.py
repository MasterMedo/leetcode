class Solution:
    def capitalizeTitle(self, title: str) -> str:
        def capitalise(word):
            if len(word) < 3:
                return word.lower()

            return word[0].upper() + word[1:].lower()

        return " ".join(map(capitalise, title.split()))
