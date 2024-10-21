from multiprocessing import Process, Pool
import requests

from time import time


#def fact(n: int):
#    if n == 1:
#        return 1
#    else:
#        return n * fact(n-1)d
#
#
#def some_activity():
#    foo = 1_000_000
#    for x in range(foo):
#        x - (x ** 3/fact(3)) + (x ** 5 / fact(5)) - (x ** 7 / fact(7)) + (x ** 9 / fact(9)) - (x ** 11 / fact(11))


def calc_sum(nums: list[int]) -> int:
    return sum(nums)


def calc_sum_print(nums: list[int]):
    return print(sum(nums))


def multiprocessed_activity(n_processes: int) -> float:
    t0 = time()
    nums = range(1_000_000)

    step = len(nums) // n_processes
    position = 0
    processes = []
    for _ in range(n_processes):
        split = list(nums[position:position+step])

        processes.append(Process(target=calc_sum, args=(split,), daemon=True))
        position += step

    for t in processes:
        t.start()
    for t in processes:
        t.join()
    return time() - t0

def pool_multiprocessed_activity(n_processes):
    t0 = time()
    nums = range(1_000_000)

    step = len(nums) // n_processes
    with Pool(n_processes) as pool:
        result = pool.map(calc_sum, [nums[position:position + step] for position in range(0, len(nums), step)])
        print(result)
    return time() - t0


if __name__ == '__main__':
    n = 10

    print(f"Threaded CPU bound task was finished in {pool_multiprocessed_activity(n)} seconds")



