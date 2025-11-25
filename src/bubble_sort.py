from typing import List


def bubble_sort(a: List[int]) -> List[int]:
    if type(a) is not list:
        raise ValueError("Аргумент должен быть списком")
    if any(type(x) is not int for x in a):
        raise ValueError("Элементы списка должны быть целыми числами")

    if not a:
        return []
    array = a[:]
    len_array = len(array)
    for i in range(len_array):
        swap = False
        for j in range(len_array - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swap = True
        if not swap:
            break

    return array


print(bubble_sort([5, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]))
