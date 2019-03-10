def quicksort(array):
    size = len(array)
    if not array or size < 2:
        return array
    pivot_idx = 0
    pivot = array[pivot_idx]
    less_part = [array[i] for i in range(size) if array[i] <= pivot and pivot_idx != i]
    great_part = [array[i] for i in range(size) if array[i] > pivot and pivot_idx != i]
    return quicksort(less_part) + [pivot] + quicksort(great_part)


def test_quicksourt():
    import random

    seq = list(range(10))
    random.shuffle(seq)
    assert quicksort(seq) == sorted(seq)


if __name__ == "main":
    test_quicksourt()
