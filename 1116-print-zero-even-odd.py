from threading import Lock


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n*2
        self.lock = Lock()
        self.zero_turn = True
        self.i = 1
        self.stop = False

    def inc(self):
        self.i += 1
        if self.i > self.n:
            self.stop = True

    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        while True:
            with self.lock:
                if self.stop:
                    break
                if self.i & 1:
                    printNumber(0)
                    self.inc()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        while True:
            with self.lock:
                if self.stop:
                    break
                if not self.i & 1 and not (self.i // 2) & 1:
                    printNumber(self.i // 2)
                    self.inc()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        while True:
            with self.lock:
                if self.stop:
                    break
                if not self.i & 1 and (self.i // 2) & 1:
                    printNumber(self.i // 2)
                    self.inc()
