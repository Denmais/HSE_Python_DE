import threading
import requests

from time import time


def activity_1():
    foo = 10000000
    for x in range(foo):
        x**2-x**2+x**4-x**5+x+x


def activity_2():
    foo = 10000000
    for x in range(foo):
        x+x


def activity_3():
    foo = 10000000
    for x in range(foo):
        x**2-x**2+x**4-x**5+x+x + x + x


def threaded_activity() -> float:
    t0 = time()
    threads = []
    threads.append(threading.Thread(target=activity_1))
    threads.append(threading.Thread(target=activity_2))
    threads.append(threading.Thread(target=activity_3))
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return time() - t0


if __name__ == '__main__':
    n = 5
    t0 = time()
    activity_1()
    activity_2()
    activity_3()
    print(f"Looped CPU bound task was finished in {time() - t0} seconds")
    print(f"Threaded CPU bound task was finished in {threaded_activity()} seconds")
