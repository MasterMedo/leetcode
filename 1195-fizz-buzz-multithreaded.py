from threading import Lock


class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.lock = Lock()
        self.i = 1
        self.stop = False

    def increase(self):
        self.i += 1
        if self.i > self.n:
            self.stop = True

    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        while True:
            with self.lock:
                if self.stop:
                    break

                if self.i % 3 == 0 and self.i % 5 != 0:
                    printFizz()
                    self.increase()

    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        while True:
            with self.lock:
                if self.stop:
                    break

                if self.i % 5 == 0 and self.i % 3 != 0:
                    printBuzz()
                    self.increase()

    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while True:
            with self.lock:
                if self.stop:
                    break

                if self.i % 3 == 0 and self.i % 5 == 0:
                    printFizzBuzz()
                    self.increase()

    def number(self, printNumber: 'Callable[[int], None]') -> None:
        while True:
            with self.lock:
                if self.stop:
                    break

                if self.i % 3 != 0 and self.i % 5 != 0:
                    printNumber(self.i)
                    self.increase()
