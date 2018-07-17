from functools import lru_cache


class Node(object):

    def __init__(self, value=None, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def __str__(self):
        return '<Node: value: {}, next={} ,prev={}>'.format(
            self.value, self.next.value, self.prev.value)

    __repr__ = __str__


class CircularDoubleLinkedList(object):
    '''
    循环双列表 ADT
    将root node的prev 指向tail节点
    '''

    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        node = Node()
        node.next, node.prev = node, node
        self.root = node
        self.length = 0

    def __len__(self):
        return self.length

    @property
    def headnode(self):
        return self.root.next

    @property
    def tailnode(self):
        return self.root.prev

    def append(self, value):
        '''O(1)'''
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception("LinkedList is full")
        node = Node(value=value)
        tailnode = self.tailnode

        tailnode.next = node
        node.prev = tailnode
        node.next = self.root
        self.root.prev = node
        self.length += 1

    def append_left(self, value):
        '''O(1)'''
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception("LinkedList is full")
        node = Node(value=value)
        headnode = self.headnode
        tailnode = self.tailnode

        node.next = headnode
        headnode.prev = node
        node.prev = self.root
        self.root.next = node
        self.length += 1

    @lru_cache()
    def find(self, value):
        '''O(n)'''
        print('in')
        for node in self.iter_node():
            if node.value == value:
                return node
        return None

    def remove(self, node):
        '''
        :param node # 在lru_cache 里根据key保存了整个node O(1)
        '''
        if node is self.root:
            return -1
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.length -= 1
            return 1

    def iter_node(self):
        if self.root.next is self.root:
            return
        curnode = self.headnode
        while curnode.next is not self.root:
            yield curnode
            curnode = curnode.next
        yield curnode

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def iter_node_reverse(self):
        '''反序遍历'''
        if self.root.next is self.root:
            return
        curnode = self.tailnode
        while curnode.prev is not self.root:
            yield curnode
            curnode = curnode.prev
        yield curnode


def test_double_link_list():
    dll = CircularDoubleLinkedList()

    assert len(dll) == 0

    dll.append(0)
    dll.append(1)
    dll.append(2)

    assert list(dll) == [0, 1, 2]

    assert [node.value for node in dll.iter_node()] == [0, 1, 2]
    assert [node.value for node in dll.iter_node_reverse()] == [2, 1, 0]

    dll.append_left(-1)
    assert list(dll) == [-1, 0, 1, 2]

    headnode = dll.headnode
    assert headnode.value == -1
    dll.remove(headnode)
    assert list(dll) == [0, 1, 2]

    node = dll.find(1)
    dll.remove(node)
    assert list(dll) == [0, 2]
