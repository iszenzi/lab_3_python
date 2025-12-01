from typing import Callable
from .math_func import factorial, factorial_recursive, fibo, fibo_recursive
from .sort import (
    bubble_sort,
    counting_sort,
    radix_sort,
    heap_sort,
    quick_sort,
    bucket_sort,
)
from .queue import Queue
from .stack import Stack
from .benchmark import benchmark_sorts


def main() -> None:
    """
    Выводит примеры работы функций, стека, очереди, бенчмарк сортировок
    :return: None
    """
    print("Факториал:")
    print("factorial(5) =", factorial(5))
    print("factorial_recursive(5) =", factorial_recursive(5))

    print("Фибоначчи:")
    print("fibo(5) =", fibo(5))
    print("fibo_recursive(5) =", fibo_recursive(5))

    print("Сортировки:")
    print("bubble_sort([5, 3, 2, 4, 1]) =", bubble_sort([5, 3, 2, 4, 1]))
    print("counting_sort([5, 3, 2, 4, 1]) =", counting_sort([5, 3, 2, 4, 1]))
    print("radix_sort([456, 123, 789, 10]) =", radix_sort([456, 123, 789, 10]))
    print("heap_sort([5, 3, 2, 4, 1]) =", heap_sort([5, 3, 2, 4, 1]))
    print("quick_sort([5, 3, 2, 4, 1]) =", quick_sort([5, 3, 2, 4, 1]))
    print(
        "bucket_sort([0.1, 0.3, 0.2, 0.4, 0.1]) =",
        bucket_sort([0.1, 0.3, 0.2, 0.4, 0.1]),
    )

    print("Стек:")
    a = Stack()
    print("Stack() =", a)
    a.push(1)
    print("Stack().push(1) =", a.data)
    a.push(2)
    print("Stack().push(2) =", a.data)
    a.push(3)
    print("Stack().push(3) =", a.data)
    print("Stack().pop() =", a.pop())
    print("Stack().peek() =", a.peek())
    print("Stack().is_empty() =", a.is_empty())
    print("Stack().__len__() =", a.__len__())
    print("Stack().min() =", a.min())

    print("Очередь:")
    b: Queue = Queue()
    print("Queue() =", b)
    b.enqueue(1)
    print("Queue().enqueue(1) =", b.data)
    b.enqueue(2)
    print("Queue().enqueue(2) =", b.data)
    b.enqueue(3)
    print("Queue().enqueue(3) =", b.data)
    print("Queue().dequeue() =", b.dequeue())
    print("Queue().front() =", b.front())
    print("Queue().is_empty() =", b.is_empty())
    print("Queue().__len__() =", b.__len__())

    print("-" * 52)
    print("Бенчмарк сортировок:")
    arrays = {
        "маленький": [5, 3, 2, 4, 1],
        "средний": [64, 34, 25, 12, 22, 11, 90, 5, 78, 56],
        "большой": [i for i in range(10000)],
        "перевернутый": list(range(20, 0, -1)),
    }

    algos: dict[str, Callable[..., list[int] | list[float]]] = {
        "bubble_sort": bubble_sort,
        "quick_sort": quick_sort,
        "heap_sort": heap_sort,
        "counting_sort": counting_sort,
        "radix_sort": radix_sort,
    }
    results = benchmark_sorts(arrays, algos)

    for array_name, algo_times in results.items():
        print(f"Массив {array_name}")
        for algo_name, elapsed_time in algo_times.items():
            if elapsed_time >= 0:
                print(f"{algo_name}: {elapsed_time:f} сек")
            else:
                print(f"{algo_name}: ошибка")

    print("Бенчмарк bucket_sort:")
    float_arrays = {
        "маленький": [0.1, 0.3, 0.9, 0.5, 0.7],
        "средний": [i / 10 for i in range(10)],
        "большой": [i / 100 for i in range(100)],
    }

    bucket_algos: dict[str, Callable[..., list[float]]] = {
        "bucket_sort (10 корзин)": lambda arr: bucket_sort(arr, buckets=10),
        "bucket_sort (50 корзин)": lambda arr: bucket_sort(arr, buckets=50),
    }

    bucket_results = benchmark_sorts(float_arrays, bucket_algos)

    for array_name, algo_times in bucket_results.items():
        print(f"Массив {array_name}")
        for algo_name, elapsed_time in algo_times.items():
            if elapsed_time >= 0:
                print(f"{algo_name}: {elapsed_time:f} сек")
            else:
                print(f"{algo_name}: ошибка")


if __name__ == "__main__":
    main()
