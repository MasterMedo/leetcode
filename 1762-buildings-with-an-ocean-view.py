class Solution:
    def findBuildings(self, heights: list[int]) -> list[int]:
        height = -1
        ocean_view = []
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > height:
                ocean_view.append(i)
                height = heights[i]

        return reversed(ocean_view)
