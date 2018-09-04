number_list = [0, 1, 2, 3, 4, 5, 6, 7]


def linear_search(value, array):
    for index, val in enumerate(array):
        if val == value:
            return index
    return -1


assert linear_search(5, number_list) == 5


def linear_search_recusive(value, array):
    if len(array) == 0:
        return -1
    index = len(array) - 1
    if array[index] == value:
        return index
    else:
        return linear_search_recusive(value, array[0:index])


assert linear_search_recusive(5, number_list) == 5
assert linear_search_recusive(8, number_list) == -1
assert linear_search_recusive(7, number_list) == 7
assert linear_search_recusive(0, number_list) == 0


def binary_search(value, array):
    if not array:
        return -1

    beg = 0
    end = len(array) - 1

    while beg <= end:
        mid = int((beg + end) / 2)
        if array[mid] == value:
            return mid
        elif array[mid] > value:
            end = mid - 1
        else:
            beg = mid + 1
    return -1


def test_binary_search():
    a = list(range(10))

    # 正常值
    assert binary_search(-1, a) == -1
    assert binary_search(1, a) == 1

    # 异常值
    assert binary_search(1, None) == -1

    # 边界值
    assert binary_search(0, a) == 0


test_binary_search()


def binary_search_recusive(value, array):
    if not array:
        return -1

    beg = 0
    end = len(array) - 1
    mid = int((beg + end) / 2)
    if mid == value:
        return mid
    elif array[mid] > value:
        return binary_search_recusive(value, array[0:mid])
    else:
        return binary_search_recusive(value, array[mid:end])


def test_binary_search_recusive():
    a = list(range(10))

    # 正常值
    assert binary_search_recusive(-1, a) == -1
    assert binary_search_recusive(1, a) == 1

    # 异常值
    assert binary_search_recusive(1, None) == -1

    # 边界值
    assert binary_search_recusive(0, a) == 0


test_binary_search_recusive()


def bisect_own(value, array):
    if not array:
        return -1

    lo = 0
    end = len(array)

    while lo < end:
        mid = int((lo + end) / 2)
        if array[mid] < value:
            lo = mid + 1
        else:
            end = mid
    return lo


def test_bisect_own():
    a = list(range(10))

    # 正常值
    assert bisect_own(-1, a) == 0
    assert bisect_own(11, a) == 10


test_bisect_own()
