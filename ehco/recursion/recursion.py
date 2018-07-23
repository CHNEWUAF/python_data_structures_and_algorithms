from collections import deque


class Stack:
    def __init__(self):
        self._deque = deque()

    def push(self, value):
        self._deque.append(value)

    def pop(self):
        return self._deque.pop()

    def is_empty(self):
        return len(self._deque) == 0


def print_num_use_stack(n):
    s = Stack()
    while n > 0:
        s.push(n)
        n -= 1
    while not s.is_empty():
        print(s.pop())


def hanoi(n, a, b, c):
    '''
    汉诺塔递归解决方法

    假设有A、B、C三个塔，
    A塔有N块盘，目标是把这些盘全部移到C塔。
    那么先把A塔顶部的N-1块盘移动到B塔
    再把A塔剩下的大盘移到C
    最后把B塔的N-1块盘移到C。

    每次移动多于一块盘时，则再次使用上述算法来移动。
    '''
    if n == 1:
        print(a, '-->', c)
    else:
        hanoi(n - 1, a, c, b)
        hanoi(1, a, b, c)
        hanoi(n - 1, b, a, c)