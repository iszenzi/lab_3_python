from typing import List


def counting_sort(a: List[int]) -> List[int]:
    if type(a) is not list:
        raise ValueError("Аргумент должен быть списком")
    if any(type(x) is not int for x in a):
        raise ValueError("Элементы списка должны быть целыми числами")

    max_number = max(a)
    min_number = min(a)

    range_numbers = max_number - min_number + 1
    count = [0] * range_numbers

    for numer in a:
        count[numer - min_number] += 1

    array_sort = []
    for i in range(range_numbers):
        array_sort.extend([i + min_number] * count[i])
    return array_sort
