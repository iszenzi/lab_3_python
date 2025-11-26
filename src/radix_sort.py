from typing import List


def radix_sort(a: List[int], base: int = 10) -> List[int]:
    if type(a) is not list:
        raise ValueError("Аргумент должен быть списком")
    if any(number < 0 for number in a) or any(type(number) is not int for number in a):
        raise ValueError("Элементы списка должны быть целыми неотрицательными числами")

    if not a:
        return []

    array = a[:]
    max_number = max(array)
    current_digit = 1

    while max_number // current_digit > 0:
        buckets: List[List[int]] = [[] for _ in range(base)]

        for number in array:
            digit = (number // current_digit) % base
            buckets[digit].append(number)

        array = [number for bucket in buckets for number in bucket]

        current_digit *= base

    return array
