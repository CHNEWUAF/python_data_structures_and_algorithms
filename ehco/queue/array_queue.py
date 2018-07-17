from array import array


class Array:
    '''定长的array'''

    def __init__(self, size=32):
        self._size = size
        self._items = [None] * size

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def __len__(self):
        return len(self._items)

    def clear(self, value=None):
        for i in range(self._items):
            self._items[i] = value

    def __iter__(self):
        for item in self._items:
            yield item


class ArrayQueue:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.array = Array(maxsize)
        self.head = 0
        self.tail = 0

    def push(self, value):
        if len(self) >= self.maxsize:
            raise Exception('queue full')
        self.array[self.head] = value
        self.head += 1

    def pop(self):
        value = self.array[self.tail % self.maxsize]
        self.tail += 1
        return value

    def __len__(self):
        return self.head - self.tail


def test_queue():
    import pytest
    size = 5
    q = ArrayQueue(size)
    for i in range(size):
        q.push(i)

    assert len(q) == 5

    assert q.pop() == 0
    assert q.pop() == 1

    assert len(q) == 3

    assert q.pop() == 2
    assert q.pop() == 3
    assert q.pop() == 4

    assert len(q) == 0
