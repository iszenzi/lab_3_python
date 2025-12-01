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


def main() -> None:
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


if __name__ == "__main__":
    main()

"""норм что в bucket_sort у меня реализована bubble_sort"""
