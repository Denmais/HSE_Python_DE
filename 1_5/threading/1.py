import threading
import time


def heavy(n, i, thead):
    for x in range(1, n):
        for y in range(1, n):
            x**y
    print(f"Цикл № {i}. Поток {thead}")


def sequential(calc, thead):
    print(f"Запускаем поток № {thead}")
    for i in range(calc):
        heavy(500, i, thead)
    print(f"{calc} циклов вычислений закончены. Поток № {thead}")


def threaded(theads, calc):

    threads = []

    for thead in range(theads):
        t = threading.Thread(target=sequential, args=(calc, thead))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


if __name__ == "__main__":
    start = time.time()
    threaded(4, 20)
    end = time.time()
    print("Общее время работы: ", end - start)
