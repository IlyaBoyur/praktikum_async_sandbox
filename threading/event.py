"""
Примитив синхронизации Event

Смысл: один поток продолжает работу ТОЛЬКО после того,
как другой поток завершил часть работы.
Если потоки работают достаточно долго, то можно наблюдать
последовательность в выполнении операций

Один поток сигнализирует о возможности продолжить работу.
Другой поток ожидает сигнала.
set() - установка в True
clear() - установка в False
wait() - блокировка потока
"""
import random, time
from threading import Event, Thread

event = Event()


def waiter(event: Event):
    for step in range(3):
        print(f'{time.ctime()}: Waiter - {step} - ожидаю сигнала...')
        event.wait()
        print(f'{time.ctime()}: Waiter - {step} - продолжаю выполнение...')
        event.clear()
        print(f'{time.ctime()}: Waiter - {step} - завершил работу...')


def trigger(event: Event):
    for step in range(3):
        print(f'{time.ctime()}: Trigger - {step} - начал работу...')
        time.sleep(random.randrange(1, 3))
        event.set()
        time.sleep(3)
        print(f'{time.ctime()}: Trigger - {step} - завершил работу...')


if __name__ == '__main__':
    threads = []
    # Cоздаём поток,который будет ожидать сигнала
    # для продолжения выполнения работы
    th = Thread(target=waiter, args=(event,))
    threads.append(th)
    th.start()
    # Cоздаём поток, который будет сигнализировать
    # о возможности продолжения работы
    th = Thread(target=trigger, args=(event,))
    threads.append(th)
    th.start()

    # Waiter продолжает выполнение только после того,
    # как Trigger начал работу 
    for thread in threads:
        thread.join()

    print('Все задачи выполнены успешно...')