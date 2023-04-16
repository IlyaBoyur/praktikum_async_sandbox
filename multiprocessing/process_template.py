from multiprocessing import Process


class Worker(Process):
    def __init__(self, func, func_args, queue):
        # Инициализация переменных
        self.func = func
        self.func_args = func_args
        self.queue = queue
        super().__init__()

    def run(self):
        # Вызов передаваемого метода и заполнение очереди
        result = self.func(*self.func_args)
        self.queue.put(result)
