class Solution:
    def areAlmostEqual(self, string_1: str, string_2: str) -> bool:
        swap_i = None
        swap_j = None
        for i in range(len(string_1)):
            if string_1[i] != string_2[i]:
                if swap_i is None:
                    swap_i = i
                elif swap_j is None:
                    swap_j = i
                else:
                    return False

        if swap_i is None:
            return True

        if swap_j is None:
            return False

        return (
            string_1[swap_i] == string_2[swap_j]
            and string_1[swap_j] == string_2[swap_i]
        )
