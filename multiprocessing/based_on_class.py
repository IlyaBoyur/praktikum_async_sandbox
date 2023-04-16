from multiprocessing import Process
from time import sleep


class CustomProcess(Process):
    def __init__(self, limit):
        super().__init__()
        self._limit = limit

    def run(self):
        for i in range(self._limit):
            print(f"Из CustomProcess: {i}")
            sleep(0.5)


if __name__ == "__main__":
    custom = CustomProcess(5)
    custom.start()
