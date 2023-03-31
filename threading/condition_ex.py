import random
import time
from threading import Condition, Thread
 
condition = Condition()
data_pool = []
 
 
def producer() -> None:
    time.sleep(3)
    condition.acquire()
    num = random.randint(100, 500)
    data_pool.append(num)
    condition.notify_all()
    print('Отправлено:', num)
    condition.release()
 
 
def consumer(consumer_id: int) -> None:
    condition.acquire()
    condition.wait()
    print(f'Consumer {consumer_id} got {data_pool[0]}')
    time.sleep(1)
    print(f'Consumer {consumer_id} finished')
    
    # Uncomment this line to see the difference
    condition.release()
 
 
if __name__ == '__main__':
    producer_thread = Thread(target=producer)
    threads = [producer_thread]
    producer_thread.start()
 
    for consumer_id in range(2):
        th = Thread(target=consumer, args=(consumer_id,))
        threads.append(th)
        th.start()
 
    for thread in threads:
        thread.join()
 
    print('Все задачи выполнены успешно...')