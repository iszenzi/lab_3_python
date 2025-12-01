import time
from typing import Mapping, Callable


def timeit_once(func, *args, **kwargs) -> float:
    """
    Измеряет время выполнения функции один раз
    :param func: Функция для измерения времени
    :param args: Позиционные аргументы для функции
    :param kwargs: Именованные аргументы для функции
    :return: Время выполнения в секундах
    """
    start = time.perf_counter()
    func(*args, **kwargs)
    end = time.perf_counter()
    return end - start


def benchmark_sorts(
    arrays: Mapping[str, list[int] | list[float]],
    algos: Mapping[str, Callable[..., list[int] | list[float]]],
) -> dict[str, dict[str, float]]:
    """
    Запускает бенчмарки сортировок для массивов и алгоритмов
    :param arrays: Словарь массивов для тестирования
    :param algos: Словарь алгоритмов сортировки
    :return: Словарь результатов вида {array_name: {algo_name: время_в_секундах}}
    """
    results: dict[str, dict[str, float]] = {}

    for array_name, array in arrays.items():
        results[array_name] = {}

        for algo_name, algo_func in algos.items():
            try:
                test_array = array[:]
                elapsed_time = timeit_once(algo_func, test_array)
                results[array_name][algo_name] = elapsed_time
            except Exception as e:
                results[array_name][algo_name] = -1.0
                print(f"Ошибка при выполнении {algo_name} на {array_name}: {e}")

    return results
