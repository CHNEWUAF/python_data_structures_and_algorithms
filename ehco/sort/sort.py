def bubble_sort(array):
    "O(n2)"
    lens = len(array) - 1
    for i in range(lens):
        for j in range(lens - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def select_sort(array):
    "O(n2)"
    lens = len(array)
    for i in range(lens):
        min_idx = i
        for j in range(i + 1, lens):
            if array[j] < array[min_idx]:
                min_idx = j
        if min_idx != i:
            array[i], array[min_idx] = array[min_idx], array[i]
    return array


def insert_sort(array):
    "O(n2)"
    lens = len(array)
    for i in range(1, lens):
        val = array[i]
        pos = i
        while pos > 0 and val < array[pos - 1]:
            # 把大的值往后移动
            array[pos] = array[pos - 1]
            pos -= 1
        array[pos] = val
    return array


def quick_sort(array):
    size = len(array)
    if not array or size < 2:
        return array
    pivot_idx = 0
    pivot = array[pivot_idx]
    less_part = [array[i] for i in range(size) if array[i] <= pivot and pivot_idx != i]
    great_part = [array[i] for i in range(size) if array[i] > pivot and pivot_idx != i]
    return quick_sort(less_part) + [pivot] + quick_sort(great_part)


def test_sort():
    import random

    seq = list(range(10))
    random.shuffle(seq)

    assert bubble_sort(seq) == sorted(seq)
    assert select_sort(seq) == sorted(seq)
    assert insert_sort(seq) == sorted(seq)
    assert quick_sort(seq) == sorted(seq)

