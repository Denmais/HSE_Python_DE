from multiprocessing import Process, Pool
import requests

from time import time


def fact(n: int):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)


def some_activity():
    foo = 1_000_000
    for x in range(foo):
        x - (x ** 3/fact(3)) + (x ** 5 / fact(5)) - (x ** 7 / fact(7)) + (x ** 9 / fact(9)) - (x ** 11 / fact(11))


def some_network_activity():
    requests.get('https://ya.ru')


def multhiprocessed_activity(n_processes: int) -> float:
    t0 = time()
    processes = [Process(target=some_activity, daemon=True) for _ in range(n_processes)]
    for t in processes:
        t.start()
    for t in processes:
        t.join()
    return time() - t0


def multiprocessed_network_activity(n_processes: int) -> float:
    t0 = time()
    processes = [Process(target=some_network_activity, daemon=True) for _ in range(n_processes)]
    for t in processes:
        t.start()
    for t in processes:
        t.join()
    return time() - t0


if __name__ == '__main__':
    n = 5
    t0 = time()
    for _ in range(n):
        some_activity()
    print(f"Looped CPU bound task was finished in {time() - t0} seconds")
    print(f"Threaded CPU bound task was finished in {multhiprocessed_activity(n)} seconds")

    n = 10
    t0 = time()
    for _ in range(n):
        some_network_activity()
    print(f"Looped IO bound task was finished in {time() - t0} seconds")
    print(f"Threaded IO bound task was finished in {multiprocessed_network_activity(n)} seconds")


