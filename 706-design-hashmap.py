class MyHashMap:
    def __init__(self):
        self.storage = [[[], set()] for _ in range(100)]

    def hash(self, key) -> int:
        return (key * 37 - 43) % 100

    def put(self, key: int, value: int) -> None:
        h = self.hash(key)
        if key in self.storage[h][1]:
            for i in range(len(self.storage[h][0])):
                if self.storage[h][0][i][0] == key:
                    self.storage[h][0][i][1] = value
                    return
        else:
            self.storage[h][0].append([key, value])
            self.storage[h][1].add(key)

    def get(self, key: int) -> int:
        h = self.hash(key)
        if key in self.storage[h][1]:
            return next(v for k, v in self.storage[h][0] if k == key)
        return -1

    def remove(self, key: int) -> None:
        h = self.hash(key)
        if key in self.storage[h][1]:
            self.storage[h][1].remove(key)
            for i in range(len(self.storage[h][0])):
                if self.storage[h][0][i][0] == key:
                    self.storage[h][0].pop(i)
                    return
