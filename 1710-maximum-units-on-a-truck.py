class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        carry = 0
        for boxes, units in boxTypes:
            if truckSize > boxes:
                truckSize -= boxes
                carry += boxes * units
            else:
                carry += truckSize * units
                break

        return carry
