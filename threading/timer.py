import random
from threading import Timer


def logger(msg: str):
    print(f"Запись в журнал: {msg}")


def reject(timer: Timer):
    timer.cancel()
    print(f"Таймер {timer.name} отменен...")


if __name__ == "__main__":
    delay = random.randrange(2, 7)
    timer1 = Timer(
        interval=delay,
        function=logger,
        args=(f"Запуск функции после задержки {delay} сек...",),
    )
    timer1.start()

    timer2 = Timer(
        interval=3, function=logger, args=("Второй таймер с сообщением",)
    )
    timer2.start()
    rejecter = Timer(interval=2, function=reject, args=(timer2,))
    rejecter.start()

    print("Программа завершена...")
