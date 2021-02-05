from threading import Lock


class H2O:
    def __init__(self):
        self.lock = Lock()
        self.arr = []

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        while True:
            with self.lock:
                if self.arr in [[], ['O'], ['O', 'H'], ['H', 'O']]:
                    self.arr.append('H')
                    if len(self.arr) >= 3:
                        self.arr = []
                else:
                    continue

            releaseHydrogen()
            break

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        while True:
            with self.lock:
                if self.arr in [[], ['H'], ['H', 'H']]:
                    self.arr.append('O')
                    if len(self.arr) >= 3:
                        self.arr = []
                else:
                    continue

            releaseOxygen()
            break
