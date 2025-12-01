def bubble_sort(a: list[int]) -> list[int]:
    """
    Алгоритм сравнивает соседние элементы и меняет их местами, если они
    находятся в неправильном порядке, пока массив не будет отсортирован
    :param a: Список целых чисел для сортировки
    :return: Отсортированный список целых чисел
    """
    if type(a) is not list:
        raise ValueError("Аргумент должен быть списком")
    if any(type(x) is not int for x in a):
        raise ValueError("Элементы списка должны быть целыми числами")

    if not a:
        return []

    array = a[:]
    len_array = len(array)
    for i in range(len_array):
        swapped = False
        for j in range(len_array - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if not swapped:
            break

    return array


def quick_sort(a: list[int]) -> list[int]:
    """
    Алгоритм выбирает опорный элемент из середины списка, разделяет список на элементы
    меньше, равные и больше опорного, рекурсивно сортирует подсписки, а потом объединяет подсписки
    :param a: Список целых чисел для сортировки
    :return: Отсортированный список целых чисел
    """
    if type(a) is not list:
        raise ValueError("Аргумент должен быть списком")
    if any(type(x) is not int for x in a):
        raise ValueError("Элементы списка должны быть целыми числами")

    array = a[:]
    if len(array) <= 1:
        return array

    pivot = array[len(array) // 2]
    left = [number for number in array if number < pivot]
    center = [number for number in array if number == pivot]
    right = [number for number in array if number > pivot]
    return quick_sort(left) + center + quick_sort(right)


def counting_sort(a: list[int]) -> list[int]:
    """
    Алгоритм подсчитывает количество  каждого из элементов списка, затем формирует отсортированный список на основе количества чисел
    :param a: Список целых чисел для сортировки
    :return: Отсортированный список целых чисел
    """
    if type(a) is not list:
        raise ValueError("Аргумент должен быть списком")
    if any(type(x) is not int for x in a):
        raise ValueError("Элементы списка должны быть целыми числами")

    if not a:
        return []

    max_number = max(a)
    min_number = min(a)

    range_numbers = max_number - min_number + 1
    count = [0] * range_numbers

    for number in a:
        count[number - min_number] += 1

    array_sort = []
    for i in range(range_numbers):
        array_sort.extend([i + min_number] * count[i])
    return array_sort


def radix_sort(a: list[int], base: int = 10) -> list[int]:
    """
    Алгоритм сортирует числа по отдельным разрядам, начиная с младшего, применяет блочную сортировку для каждого разряда
    :param a: Список неотрицательных целых чисел для сортировки
    :param base: Основание системы счисления (по умолчанию 10)
    :return: Отсортированный список неотрицательных целых чисел
    """
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
        buckets: list[list[int]] = [[] for _ in range(base)]

        for number in array:
            digit = (number // current_digit) % base
            buckets[digit].append(number)

        array = [number for bucket in buckets for number in bucket]

        current_digit *= base

    return array


def bucket_sort(a: list[float], buckets: int | None = None) -> list[float]:
    """
    Алгоритм распределяет элементы списка по корзинам, затем сортирует каждую корзину пузырьковой сортировкой и объединяет результаты
    :param a: Список вещественных чисел в диапазоне [0, 1) для сортировки
    :param buckets: Количество корзин
    :return: Отсортированный список вещественных чисел
    """
    if type(a) is not list:
        raise ValueError("Аргумент должен быть списком")
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

    buckets_list: list[list[float]] = [[] for _ in range(count_buckets)]

    for number in array:
        index = int(number * count_buckets)
        buckets_list[index].append(number)

    for bucket in buckets_list:
        for i in range(len(bucket)):
            swapped = False
            for j in range(len(bucket) - i - 1):
                if bucket[j] > bucket[j + 1]:
                    bucket[j], bucket[j + 1] = bucket[j + 1], bucket[j]
                    swapped = True
            if not swapped:
                break

    result = []

    for bucket in buckets_list:
        result.extend(bucket)

    return result


def shift_down(array: list[int], start: int, end: int) -> None:
    """
    Вспомогательная функция для heap_sort, перемещает элемент вниз по дереву до тех пор, пока он не займет правильную позицию
    :param array: Список, представляющий бинарную кучу
    :param start: Индекс корневого элемента для просеивания
    :param end: Индекс последнего элемента в куче
    :return: None
    """
    root = start
    while True:
        child = root * 2 + 1
        if child > end:
            break

        if child + 1 <= end and array[child] < array[child + 1]:
            child += 1

        if array[root] < array[child]:
            array[root], array[child] = array[child], array[root]
            root = child
        else:
            break


def heap_sort(a: list[int]) -> list[int]:
    """
    Алгоритм  извлекает максимальный элемент из списка и помещает его в конец отсортированной части, пока список не будет отсортирован
    :param a: Список целых чисел для сортировки
    :return: Отсортированный список целых чисел
    """
    if type(a) is not list:
        raise ValueError("Аргумент должен быть списком")
    if any(type(x) is not int for x in a):
        raise ValueError("Элементы списка должны быть целыми числами")

    if not a:
        return []

    array = a[:]

    for start in range((len(array) - 2) // 2, -1, -1):
        shift_down(array, start, len(array) - 1)

    for end in range(len(array) - 1, 0, -1):
        array[0], array[end] = array[end], array[0]
        shift_down(array, 0, end - 1)

    return array
