import time
from threading import Thread, current_thread


def custom_func(n):
    th = current_thread()
    print(f'{th.name} started')

    for _ in range(n):
        time.sleep(1)
        print(f'{th.name} still alive')

    print(f'{th.name} finished')


if __name__ == '__main__':
    main_thread = current_thread()
    print(f'{main_thread.name} started')

    child_thread = Thread(name='ChildThread', target=custom_func, args=(5,), daemon=False)
    child_thread.daemon = True 
    child_thread.start()
    # Активный поток: будет выброшено исключение RuntimeError:
    # cannot set daemon status of active thread
    # child_thread.daemon = True

    print(f'{main_thread.name} finished') 