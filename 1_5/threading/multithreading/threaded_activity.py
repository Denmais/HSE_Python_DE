import threading
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


def threaded_activity(n_threads: int) -> float:
    t0 = time()
    threads = [threading.Thread(target=some_activity, daemon=True) for _ in range(n_threads)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return time() - t0


def threaded_network_activity(n_threads: int) -> float:
    t0 = time()
    threads = [threading.Thread(target=some_network_activity, daemon=True) for _ in range(n_threads)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return time() - t0


if __name__ == '__main__':
    # n = 5
    # t0 = time()
    # for _ in range(n):
    #     some_activity()
    # print(f"Looped CPU bound task was finished in {time() - t0} seconds")
    # print(f"Threaded CPU bound task was finished in {threaded_activity(n)} seconds")

    n = 10
    t0 = time()
    for _ in range(n):
        some_network_activity()
    print(f"Looped IO bound task was finished in {time() - t0} seconds")
    print(f"Threaded IO bound task was finished in {threaded_network_activity(n)} seconds")