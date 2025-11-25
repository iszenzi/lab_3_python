from typing import List


def quick_sort(a: List[int]) -> List[int]:
    if type(a) is not list:
        raise ValueError("Аргумент должен быть списком")
    if any(type(x) is not int for x in a):
        raise ValueError("Элементы списка должны быть целыми числами")

    array = a[:]
    if len(array) <= 1:
        return array

    pivot = array[0]
    left = [number for number in array if number < pivot]
    center = [number for number in array if number == pivot]
    right = [number for number in array if number > pivot]
    return quick_sort(left) + center + quick_sort(right)
