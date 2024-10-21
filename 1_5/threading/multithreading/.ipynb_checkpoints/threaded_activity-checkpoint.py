import threading
from time import time 


def fact(n: int):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)
        
def some_activity():
    foo = 1_000_000
    t0 = time()
    for x in range(foo):
        x - (x ** 3/fact(3)) + (x ** 5 / fact(5)) - (x ** 7 / fact(7)) + (x ** 9 / fact(9)) - (x ** 11 / fact(11))
    print(time() - t0)

def threaded_activity(n_threads: int) -> float:
    t0 = time()
    threads = [threading.Thread(target=some_activity) for _ in range(n_threads)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return time() - t0

if __name__ == '__main__':
    threaded_activity(10)