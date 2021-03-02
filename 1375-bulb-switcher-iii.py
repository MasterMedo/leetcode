class Solution:
    def numTimesAllBlue(self, light: list[int]) -> int:
        on = 0
        max_ = 0
        blue = 0
        for switch in light:
            on += 1
            if switch > max_:
                max_ = switch

            if max_ == on:
                blue += 1

        return blue
