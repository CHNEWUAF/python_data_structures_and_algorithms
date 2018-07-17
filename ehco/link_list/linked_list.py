class Node(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return '<Node: value: {}, next={}>'.format(self.value, self.next.value)

    __repr__ = __str__


class LinkedList(object):
    '''
    链表 ADT
    [root] -> [node0] -> [node1] -> [node2]
    '''

    def __init__(self, maxsize=None):
        '''
        :param maxsize: int or None 如果是none 无限扩充
        '''
        self.maxsize = maxsize
        # 默认的root节点， 指向none
        self.root = Node()
        self.tailnode = None
        self.length = 0

    def __len__(self):
        return self.length

    def append(self, value):
        '''O(1)'''
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception('LinkedList is full')
        # 构造节点
        node = Node(value)
        tailnode = self.tailnode
        # 如果还没有节点append过，length = 0 将本次append的node 和root节点关联
        if tailnode is None:
            self.root.next = node
        # 否则就追加到最后一个节点的后面，并且设置新的tailnode
        else:
            tailnode.next = node
        self.tailnode = node
        self.length += 1

    def append_left(self, value):
        '''O(1)'''
        headnode = self.root.next
        node = Node(value)
        self.root.next = node
        node.next = headnode
        self.length += 1

    def iter_node(self):
        '''
        遍历从head到tail的节点
        '''
        # 从第一个节点开始遍历
        curnode = self.root.next
        while curnode is not self.tailnode:
            yield curnode
            curnode = curnode.next
        yield curnode

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def remove(self, value):
        '''
        删除包含指定值的一个节点 O(n)
        '''
        prenode = self.root
        curnode = self.root.next
        for node in self.iter_node():
            if curnode.value == value:
                prenode.next = curnode.next
                del curnode
                self.length -= 1
                # 表明删除成功
                return 1
            # 表明删除失败
            return -1

    def find(self, value):
        '''
        查找一个包含固定值的节点 并返回该节点的序号 从0开始 O(n)
        '''
        index = 0
        for node in self.iter_node():
            if node.value == value:
                return index
            index += 1
        return -1

    def pop_left(self):
        '''
        pop成链表的第一个节点 O(1)
        '''
        if self.root.next is None:
            raise Exception('pop from empty LinkedList')
        headnode = self.root.next
        self.root.next = headnode.next
        self.length -= 1
        value = headnode.value
        del headnode
        return value

    def clear(self):
        for node in self.iter_node():
            del node
        self.root.next = None
        self.length = 0

    def insert(self, value, new_value):
        '''
        在某个值之前插入一个node O(n)
        '''
        prenode = self.root
        for curnode in self.iter_node():
            if curnode.value == value:
                node = Node(value=new_value)
                prenode.next = node
                node.next = curnode
                self.length += 1
            prenode = curnode


def test_linked_list():
    ll = LinkedList(maxsize=3)

    ll.append(0)
    ll.append(1)
    ll.append(2)
    ll.append(4)

    assert len(ll) == 3
    assert ll.find(2) == 2
    assert ll.find(3) == -1

    assert ll.remove(0) == 1
    assert ll.remove(3) == -1
    assert ll.find(0) == -1

    assert list(ll) == [1, 2]

    ll.append_left(0)
    assert list(ll) == [0, 1, 2]
    assert len(ll) == 3

    headvalue = ll.pop_left()
    assert headvalue == 0
    assert len(ll) == 2
    assert list(ll) == [1, 2]

    ll.insert(1, -1)
    assert list(ll) == [-1, 1, 2]
    ll.clear()
    assert len(ll) == 0
