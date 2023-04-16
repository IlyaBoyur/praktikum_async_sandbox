"""
Класс Range2 является "итерабельным" И итератором одновременно
"""


class Range2:
    def __init__(self, stop_value: int):
        self.current = -1
        self.stop_value = stop_value - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.stop_value:
            self.current += 1
            return self.current
        raise StopIteration


def test_range():
    assert [_ for _ in Range2(5)] == [_ for _ in range(5)]
    assert list(Range2(5)) == list(range(5))
    print(*[_ for _ in Range2(5)])
    print("test succeeded")


if __name__ == "__main__":
    test_range()
