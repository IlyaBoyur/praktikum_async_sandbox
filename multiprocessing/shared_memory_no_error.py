"""
Процессы не имеют общей памяти

Изменение переменной в дочернем процессе не меняет её в основном процессе.
"""
from multiprocessing import Process, current_process


L = [0] * 10


def func():
    current = current_process()
    name = current.name
    pid = current.pid
    print(f"Процесс {name} с pid={pid} запущен")
    for i in range(len(L)):
        L[i] = i
    print(f"Пишу в дочернем процессе, L: {L}")
    print(f"Процесс {name} с pid={pid} завершен")

if __name__ == "__main__":
    process = Process(name="Дочка", target=func)
    current = current_process()
    name = current.name
    pid = current.pid

    print(f"Процесс {name} с pid={pid} запущен")
    L.extend([1,2,3,4,5])

    process.start()

    
    process.join()
    print(f"Смотрим L: {L}")

    print(f"Процесс {name} с pid={pid} завершен")
