from collections import OrderedDict


class Node:
    def __init__(self, value=None, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

    def __str__(self):
        return f"<Node: value: {self.value}>"

    __repr__ = __str__


class DBL:
    def __init__(self):
        node = Node("root")
        node.prev = node
        node.next = node
        self.root = node

        self.lens = 0

    @property
    def head(self):
        return self.root.next

    @property
    def tail(self):
        return self.root.prev

    def append(self, value):
        node = Node(value)

        self.tail.next = node
        node.prev = self.tail
        node.next = self.root
        self.root.prev = node
        self.lens += 1

    def append_left(self, value):
        node = Node(value)

        node.next = self.head
        self.head.prev = node
        self.root.next = node
        node.prev = self.root
        self.lens += 1

    def remove(self, node):
        # NOTE for spec case
        if node == self.root:
            return False
        if node == self.tail:
            self.root.prev = node.prev
        if node.next:
            node.next.prev = node.prev
        node.prev.next = node.next
        del node
        self.lens -= 1
        return True

    def iter_item(self):
        cur = self.root.next
        while cur and cur != self.root:
            yield cur
            cur = cur.next

    def find(self, value):
        for node in self.iter_item():
            if node.value == value:
                return node
        return None

    def insert(self, value, new_value):
        per = self.root
        for node in self.iter_item():
            if node.value == value:
                temp = Node(new_value)
                per.next = temp
                temp.prev = per
                temp.next = node
                node.prev = temp
                self.lens += 1
                return True
            per = node
        self.append(new_value)

    def __str__(self):
        return "->".join([str(node.value) for node in self.iter_item()])

    __repr__ = __str__


class LRU:
    def __init__(self, size=10):
        self.size = size
        self._link = DBL()
        self._cache = dict()

    def _move_to_recent(self, node):
        if node == self._link.tail:
            return

        # pop node from link
        node.prev.next = node.next
        node.next.prev = node.prev
        # set node to tail
        now_tail = self._link.tail
        now_tail.next = node
        node.prev = now_tail
        node.next = None
        self._link.root.prev = node

    def _append(self, k, v):
        self._link.append(v)
        self._cache[k] = self._link.tail
        # Bind cache key
        self._link.tail.cache_key = k

    def _expired_not_used(self):
        need_expired = self._link.head
        self._link.remove(need_expired)

    def get(self, k):
        node = self._cache.pop(k, None)
        if not node:
            return
        self._move_to_recent(node)
        return node.value

    def put(self, k, v):
        node = self._cache.pop(k, None)
        if node:
            node.value = v
            self._move_to_recent(node)
        else:
            if self._link.lens == self.size:
                self._expired_not_used()
            self._append(k, v)

    def __str__(self):
        return "->".join([f"{node.cache_key}" for node in self._link.iter_item()])

    __repr__ = __str__


class OLRU:
    def __init__(self, size=10):
        self._cache = OrderedDict()
        self.size = size

    def get(self, k):
        ret = self._cache.pop(k, None)
        if ret:
            self._cache[k] = ret
        return ret

    def put(self, k, v):
        ret = self._cache.pop(k, None)
        if not ret and len(self._cache) == self.size:
            # NOTE pop last recent used item
            self._cache.popitem(False)
        self._cache[k] = v


def test_lru():
    lru = LRU(size=10)

    for i in range(10):
        lru.put(i, i)

    for i in range(10):
        assert lru.get(i) == i

    print(lru)
    lru.put(11, 11)
    assert lru.get(11) == 11
    print(lru)

    assert lru.get(0) == None

    for i in range(100):
        lru.put(i, i)
    print(lru)
