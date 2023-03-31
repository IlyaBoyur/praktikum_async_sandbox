"""
Класс Range является "итерабельным" - реализует метод __iter__
Класс RangeIterator является итератором, или итерируемым объектом
"""
class Range:
    def __init__(self, stop_value: int):
        self.current = -1
        self.stop_value = stop_value - 1
  
    def __iter__(self):
        return RangeIterator(self)
  
class RangeIterator:
    def __init__(self, container):
        self.container = container
  
    def __next__(self):
        if self.container.current < self.container.stop_value:
            self.container.current += 1
            return self.container.current
        raise StopIteration


def test_range():
    assert [_ for _ in Range(5)] == [i for i in range(5)]
    assert list(Range(5)) == list(range(5))
    print("test succeeded")

if __name__ == "__main__":
    test_range()