class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        flag = False
        i = 0
        while i != len(bits):
            if bits[i] == 1:
                i += 2
                flag = False
            else:
                i += 1
                flag = True

        return flag
