"""
Задача: циклический итератор
Итератор должен итерироваться по итерируемому объекту:
list, tuple, set, range, Range2.
А когда он достигнет последнего элемента, начинать сначала.

cyclic_iterator = CyclicIterator(range(3))
for i in cyclic_iterator:
    print(i) 

Вывод:
0
1
2
0
1
2
0
1
2
.... 
"""
import typing


class CyclicGen:
    """Class object is iterable"""

    def __init__(self, iterable):
        self.iterable = iterable

    def __iter__(self):
        while True:
            iterator = iter(self.iterable)
            for i in iterator:
                yield i


class CyclicIterator:
    """Class object is iterable AND is iterator"""

    def __init__(self, iterable):
        self.iterable = iterable
        self.iterator = iter(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.iterator)
        except StopIteration:
            self.iterator = iter(self.iterable)
            return next(self.iterator)


def test_cyclic_iterator():
    cyclic_iterator = CyclicIterator(range(3))

    for _ in range(4):
        print(next(cyclic_iterator), end=" ")
    print()
    print("test succeeded")


if __name__ == "__main__":
    test_cyclic_iterator()
