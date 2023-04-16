"""
Задача: разжатие массива
У каждого фильма есть расписание, по каким дням он идёт в кинотеатрах.
Для эффективности дни проката хранятся периодами дат.
Например, прокат фильма проходит с 1 по 7 января, а потом показ возобновляется с 15 января по 7 февраля: 

[(datetime(2020, 1, 1), datetime(2020, 1, 7)), (datetime(2020, 1, 15), datetime(2020, 2, 7))] 

Ожидаемый вывод программы:
2020-01-01 00:00:00
2020-01-02 00:00:00
...
2020-01-06 00:00:00
2020-01-07 00:00:00
2020-01-15 00:00:00
2020-01-16 00:00:00
...
2020-01-31 00:00:00
2020-02-01 00:00:00
2020-02-02 00:00:00
...
2020-02-07 00:00:00 
"""
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Generator


@dataclass
class Movie:
    title: str
    dates: list[tuple[datetime, datetime]]

    def schedule(self) -> Generator[datetime, None, None]:
        for start, end in self.dates:
            now = start
            while now <= end:
                yield now
                now += timedelta(days=1)


if __name__ == "__main__":
    movie = Movie(
        "Star Wars",
        [
            (datetime(2020, 1, 1), datetime(2020, 1, 7)),
            (datetime(2020, 1, 15), datetime(2020, 2, 7)),
        ],
    )

    for date in movie.schedule():
        print(date)
