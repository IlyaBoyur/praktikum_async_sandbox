import math


def cash_return_coro(percent: float, years: int) -> float:
    """Calculate deposit return"""
    value = math.pow(1 + percent / 100, years)
    while True:
        try:
            deposit = (yield)
            yield round(deposit * value, 2)
        except GeneratorExit:
            print('Выход из корутины')
            raise


if __name__ == "__main__":
    coro = cash_return_coro(5, 5)
    next(coro)
    for item in [1000, 2000, 5000, 10000, 100000]:
        print(coro.send(item))
        next(coro)
    coro.close()
