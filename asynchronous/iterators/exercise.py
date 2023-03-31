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


class CyclicIteratorGen:
    def __init__(self, iterable):
        self.iterable = iterable

    def __iter__(self):
        while True:
            iterator = iter(self.iterable)
            for i in iterator:
                yield i


class CyclicIterator:
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

if __name__ == "__main__":
    cyclic_iterator = CyclicIterator(range(3))
    # cyclic_iterator = CyclicIterator(list(range(3)))
    # cyclic_iterator = CyclicIterator(tuple(range(3)))
    # cyclic_iterator = CyclicIterator(set(range(3)))
    iterable = iter(cyclic_iterator)
    print(next(iterable))
    print(next(iterable))
    print(next(iterable))
    print(next(iterable))

    # print(next(cyclic_iterator))