class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        provinces = [{0}]
        for i in range(1, len(isConnected)):
            connected = []
            for p, province in enumerate(provinces):
                for j in province:
                    if isConnected[i][j]:
                        connected.append(p)
                        break
            province = {i}
            for p in reversed(connected):
                province = province | provinces.pop(p)
            provinces.append(province)
        return len(provinces)
