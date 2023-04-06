from task import Task

def double(x):
    yield x * x


def add(x, y):
    yield from double(x + y)


def main():
    result = yield add(1, 2)
    print(result)
    yield


if __name__ == "__main__":
    task = Task(main())
    task.run()
