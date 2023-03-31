from concurrent.futures import ThreadPoolExecutor

data = range(1, 15)
pool_size = 5

def f1(item):
    """Возведение в квадрат"""
    return item ** 2

def f2(data):
    """Подсчёт суммы элементов массива"""
    return sum(data)

def worker(data):
    """
    Возведение всех элементов массива в квадрат и
    подсчёт суммы всех элементов
    """
    with ThreadPoolExecutor(max_workers=pool_size) as pool:
        # Взаимодействие с пулом для возведения в квадрат и подсчёта суммы всех элементов
        squares = pool.map(f1, data)
        future = pool.submit(f2, squares)
    
    return future.result()

if __name__ == "__main__":
    print(f"Результат: {worker(data)}")
