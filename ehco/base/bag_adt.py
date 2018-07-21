class Bag:

    def __init__(self, max_size=10):
        self.max_size = max_size
        self._items = list()

    def add(self, item):
        if len(self._items) >= self.max_size:
            raise Exception('Bag is Full')
        self._items.append(item)

    def remove(self, item):
        self._items.remove(item)

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        for item in self._items:
            yield item


def test_bag():
    bag = Bag()

    for i in range(10):
        bag.add(i)

    bag.remove(3)
    assert len(bag) == 9

    bag.add(1)
    assert len(bag) == 10

    try:
        bag.add(1)
        print('len', len(bag))
    except Exception as e:
        print(e)

    for i in bag:
        print(i)


if __name__ == '__main__':
    test_bag()
