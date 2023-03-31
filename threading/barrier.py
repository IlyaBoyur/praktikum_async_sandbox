"""
Примитив синхронизации Barrier

Смысл: 1..N потоков вызывают wait() ждут друг друга, прежде чем продолжить.
Число потоков определяется в примитиве при его создании.
Пример: игрок делает ход только когда все остальные игроки завершили подготовку. 
"""
from random import randrange
from threading import Barrier, Thread
from time import sleep, ctime


participants = ['Борис', 'Олег', 'Слава', 'Петр']
threads_count = len(participants)
b = Barrier(threads_count)


def start_game():
    player = participants.pop()
    sleeping_time = randrange(2, 5)
    print(f'Игрок {player} начал подготовку: {sleeping_time}')
    sleep(sleeping_time)
    print(f'Игрок {player} завершил: {ctime()}')
    b.wait()
    print(f"Игрок {player} ходит!")


if __name__ == '__main__':
    threads = []
    print('Начало игры...')
    for i in range(threads_count):
        th = Thread(target=start_game)
        threads.append(th)
        th.start()

    for thread in threads:
        thread.join()
    print('Игра окончена')

