"""
Примитив синхронизации Lock 
Смысл: простейший примитив,
используется для защиты от изменения общей переменной
одновременно из нескольких потоков.

Как только поток получил блокировку, последующие попытки получить его блокируются,
пока объект примитива не будет разблокирован.
"""
import threading
import time

thread_lock = threading.Lock()


class MyThread(threading.Thread):
    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay

    def run(self):
        print(f'Запущен поток {self.name}')
        thread_lock.acquire()
        try:
            thread_count_down(self.name, self.delay)
        finally:
            thread_lock.release()
        time.sleep(1)
        print(f'Завершен поток {self.name}')


def thread_count_down(name, delay):
    counter = 7
    while counter:
        time.sleep(delay)
        print(f'Поток {name} - {counter}...')
        counter -= 1


if __name__ == '__main__':
    thread1 = MyThread('Thread-1', 0.5)
    thread2 = MyThread('Thread-2', 0.2)

    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

    print('Завершаем работу.') 