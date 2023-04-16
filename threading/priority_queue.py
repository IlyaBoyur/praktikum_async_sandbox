from queue import PriorityQueue
from random import randint, random
from threading import Thread
from time import sleep


def producer(queue):
    print("Producer: начало работы")
    for idx in range(5):
        data = random()
        priority = randint(0, 5)
        task = (priority, data)
        queue.put(task)
        print(f"Producer: в очередь добавлен элемент [{task}]")
    queue.join()
    queue.put(None)
    print("Producer: завершение работы")


def consumer(queue):
    print("Consumer: начало работы")
    while True:
        task = queue.get()
        if task is None:
            break
        sleep(1)
        print(f"Consumer: обработан элемент {task}")
        queue.task_done()
    print("Consumer: завершение работы")


queue = PriorityQueue()
producer_ = Thread(target=producer, args=(queue,))
producer_.start()

consumer_ = Thread(target=consumer, args=(queue,))
consumer_.start()

producer_.join()
consumer_.join()
