import multiprocessing
import random
import time


class Producer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        for idx in range(5):
            item = random.randint(0, 100)
            self.queue.put(item)
            print(f"Producer: запись {item} добавлена {self.name}\n")
            time.sleep(1)
            print(f"Queue size: {self.queue.qsize()}")


class Consumer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            if self.queue.empty():
                print("Очередь пуста")
                break
            else:
                time.sleep(1)
                item = self.queue.get()
                print(f"Consumer: запись {item} получена из {self.name} \n")
                time.sleep(1)


if __name__ == "__main__":
    queue = multiprocessing.Queue()
    process_producer = Producer(queue)
    process_consumer = Consumer(queue)
    process_producer.start()
    process_consumer.start()
    process_producer.join()
    process_consumer.join()
