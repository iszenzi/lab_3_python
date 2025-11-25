from typing import List


def bubble_sort(a: List[int]) -> List[int]:
    if not a:
        return []
    array = a[:]
    len_array = len(array)
    for i in range(len_array):
        for j in range(len_array - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array
