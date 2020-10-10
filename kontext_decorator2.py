import time

class Timer:
    def __init__(self, num_runs=1):
        self.num_runs = num_runs

    def __enter__(self, *args):
        self.start = time.time()
        return self.start

    def __exit__(self, *args):
        self.stop = time.time()
        print("Выполнение заняло %.5f секунд" % (self.stop - self.start))

    def __call__(self, func):
        def timer():
            avg_time = 0
            for _ in range(self.num_runs):
                t0 = time.time()
                func()
                t1 = time.time()
                avg_time += (t1 - t0)
            avg_time /= self.num_runs
            print("Выполнение заняло %.5f секунд" % avg_time)

        return timer

obj = Timer(num_runs = 10)

@obj
def f():
    for i in range(1000000):
        pass


if __name__ == "__main__":
    obj = Timer(num_runs = 10)
    @obj
    def f():
        for i in range(1000000):
            pass
    print("Тестируем объект, как декоратор")
    f()

    print("Тестируем объект, как контекстный менеджер")
    with Timer() as t:
        a = list(range(1000000, 1, -1))
        a.sort()



