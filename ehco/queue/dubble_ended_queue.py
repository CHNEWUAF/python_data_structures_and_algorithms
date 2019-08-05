from ehco.link_list.lru import DBL


class Dequeue:
    def __init__(self):
        self._double_link_list = DBL()

    @property
    def head(self):
        return self._double_link_list.head

    @property
    def tail(self):
        return self._double_link_list.tail

    def append(self, val):
        self._double_link_list.append(val)

    def append_left(self, val):
        self._double_link_list.append_left(val)

    def pop(self):
        node = self.tail
        res = self._double_link_list.remove(node)
        if res:
            return node.value

    def pop_left(self):
        node = self.head
        res = self._double_link_list.remove(node)
        if res:
            return node.value


def test_double_ended_queue():
    deq = Dequeue()

    for i in range(10):
        deq.append(i)

    for i in range(10):
        assert deq.pop_left() == i

    for i in range(10):
        deq.append_left(i)

    for i in range(10):
        assert deq.pop() == i

