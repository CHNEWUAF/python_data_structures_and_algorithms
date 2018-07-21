from ehco.hashtable.hashtable_adt import HashTable


class Set(HashTable):

    def add(self, key):
        return super(Set, self).add(key, True)

    def remove(self, key):
        super(Set, self).remove(key)

    def pop(self):
        if len(self) == 0:
            raise Exception('pop from emepty set')
        key = list(self)[-1]
        super(Set, self).remove(key)
        return key

    def __and__(self, other_set):
        '''取交集'''
        new_set = Set()
        for ele_a in self:
            if ele_a in other_set:
                new_set.add(ele_a)
        return new_set

    def __sub__(self, other_set):
        '''取差集'''
        new_set = Set()
        for ele_a in self:
            if ele_a not in other_set:
                new_set.add(ele_a)
        return new_set

    def __or__(self, other_set):
        '''取并集'''
        new_set = Set()
        for ele_a in self:
            new_set.add(ele_a)
        for ele_b in other_set:
            new_set.add(ele_b)
        return new_set

    def __xor__(self, other_set):
        '''取对称差'''
        new_set = (self | other_set) - (self & other_set)
        return new_set


def test_set():
    s1 = Set()
    s1.add(1)
    s1.add(2)
    s1.add(3)
    assert 1 in s1

    s1.add(1)
    assert len(s1) == 3

    s2 = Set()
    s2.add(3)
    s2.add(4)
    s2.add(5)

    assert sorted(list(s1 & s2)) == [3]
    assert sorted(list(s1 - s2)) == [1, 2]
    assert sorted(list(s1 | s2)) == [1, 2, 3, 4, 5]
    assert sorted(list(s1 ^ s2)) == [1, 2, 4, 5]

    assert s1.remove(1) is True
    assert s1.remove(5) is False
