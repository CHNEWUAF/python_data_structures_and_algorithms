from ehco.queue.dubble_ended_queue import Dequeue


class Stack:
    def __init__(self):
        self._dequeue = Dequeue()
        self.lens = 0

    def push(self, value):
        self._dequeue.append(value)
        self.lens += 1

    def pop(self):
        if self.lens > 0:
            self.lens -= 1
            return self._dequeue.pop()


class MinMaxStack:
    def __init__(self):
        self._stack = Stack()
        self._min_stack = Stack()
        self._max_stack = Stack()

    def push(self, value):
        self._stack.push(value)
        if self._min_stack.lens == 0:
            self._min_stack.push(value)
        else:
            if value < self.min:
                self._min_stack.push(value)

        if self._max_stack.lens == 0:
            self._max_stack.push(value)
        else:
            if value > self.max:
                self._max_stack.push(value)

    def pop(self):
        val = self._stack.pop()
        now_min = self._min_stack.pop()
        if val != now_min:
            self._min_stack.push(now_min)

        now_max = self._max_stack.pop()
        if val != now_max:
            self._max_stack.push(now_max)
        return val

    @property
    def min(self):
        value = self._min_stack.pop()
        if value is not None:
            self._min_stack.push(value)
        return value

    @property
    def max(self):
        value = self._max_stack.pop()
        if value is not None:
            self._max_stack.push(value)
        return value


def test_stack():
    s = Stack()
    s.push(0)
    s.push(1)
    s.push(2)

    assert s.pop() == 2
    assert s.pop() == 1
    assert s.pop() == 0


def test_min_max_stack():
    s = MinMaxStack()
    s.push(0)
    s.push(1)
    s.push(2)

    assert s.max == 2
    assert s.min == 0

    assert s.pop() == 2
    assert s.max == 1
    assert s.min == 0

    s.push(-1)
    assert s.max == 1
    assert s.min == -1

