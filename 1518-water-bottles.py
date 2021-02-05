class Solution:
    def numWaterBottles(self, water: int, price: int) -> int:
        empty = 0
        drank = 0
        while True:
            if water:
                empty += water
                drank += water
                water = 0
            elif empty >= price:
                water, empty = divmod(empty, price)
            else:
                break

        return drank
