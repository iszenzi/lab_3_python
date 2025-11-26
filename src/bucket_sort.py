from typing import List


def bucket_sort(a: List[float], buckets: int | None = None) -> List[float]:
    if any(x < 0.0 or x >= 1.0 for x in a):
        raise ValueError("Элементы списка должны быть в диапазоне [0, 1)")

    if not a:
        return []

    array = a[:]

    if buckets is not None:
        count_buckets = buckets
    else:
        count_buckets = len(array)

    if count_buckets <= 0:
        count_buckets = 1

    buckets_list: List[List[float]] = [[] for _ in range(count_buckets)]

    for number in array:
        index = int(number * count_buckets)
        buckets_list[index].append(number)

    for bucket in buckets_list:
        for i in range(len(bucket)):
            swap = False
            for j in range(len(bucket) - i - 1):
                if bucket[j] > bucket[j + 1]:
                    bucket[j], bucket[j + 1] = bucket[j + 1], bucket[j]
                    swap = True
            if not swap:
                break

    result = []

    for bucket in buckets_list:
        result.extend(bucket)

    return result
