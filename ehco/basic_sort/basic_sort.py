import random


def bubble_sort(seq):
    '''O(n^2)'''
    n = len(seq)

    for i in range(n-1):
        print(seq)
        for j in range(n-1-i):
            if seq[j] > seq[j+1]:
                seq[j], seq[j+1] = seq[j+1], seq[j]
        print('+++++++++++++bubble++++++++++++++')
    return seq


def select_sort(seq):
    '''O(n)'''
    n = len(seq)

    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if seq[j] < seq[min_idx]:
                min_idx = j
        if min_idx != i:
            seq[i], seq[min_idx] = seq[min_idx], seq[i]
        print(seq)
        print('+++++++++++++select++++++++++++++')
    return seq


def insert_sort(seq):
    '''O(n)'''
    n = len(seq)

    for i in range(0, n):
        v = seq[i]
        pos = i
        while pos > 0 and v < seq[pos-1]:
            seq[pos] = seq[pos-1]
            pos -= 1
        seq[pos] = v
        print('+++++++++++++insert++++++++++++++')
    return seq


def test_sort():
    seq = list(range(10))
    random.shuffle(seq)

    assert bubble_sort(seq[:]) == sorted(seq)
    print("\n\n")
    assert select_sort(seq[:]) == sorted(seq)
    print("\n\n")
    assert insert_sort(seq[:]) == sorted(seq)


if __name__ == "__main__":
    test_sort()
