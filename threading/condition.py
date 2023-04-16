"""
Примитив синхронизации Condition

Смысл: примитив позволяет организовать совместный доступ к ресурсу.

Как работает: внутри примитива заложен Lock объект.
Пока один поток владеет внутренним Lock объектом примитива, другие потоки ждут.
"""
import random
import time
from threading import Condition, Thread

condition = Condition()
data_pool = []


def producer(data_pool, pool_size):
    for i in range(pool_size):
        time.sleep(random.randrange(1, 3))
        # Ждём внутренний Lock
        condition.acquire()
        num = random.randint(100, 500)
        data_pool.append(num)
        # Сигнализируем о возможности продолжить работу
        # При замене на .notify_all(), сигнал о продолжении получат все потоки,
        # подписанные и ожидающие текущий триггер
        condition.notify()
        print("Отправлено:", num)
        # Отпускаем внутренний Lock
        condition.release()


def consumer(data_pool, pool_size):
    for i in range(pool_size):
        # Ждём внутренний Lock
        condition.acquire()
        # Отпускаем внутренний Lock
        # Ожидаем сигнал о возможности продолжения работы
        condition.wait()
        # Где-то в другом потоке вызван notify / notify_all и отпущен внутренний Lock,
        # захватываем внутренний Lock
        print("%s: Получено: %s" % (time.ctime(), data_pool.pop()))
        # Отпускаем внутренний Lock
        condition.release()


if __name__ == "__main__":
    threads = []
    threads_max = random.randrange(2, 7)

    print(f"Всего посылок: {threads_max}")

    for func in [producer, consumer]:
        th = Thread(target=func, args=(data_pool, threads_max))
        threads.append(th)
        th.start()

    for thread in threads:
        thread.join()

    print("Все посылки отправлены и получены!")
