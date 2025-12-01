class Queue:
    def __init__(self) -> None:
        self.data: list[int] = []

    def enqueue(self, x: int) -> None:
        if type(x) is not int:
            raise ValueError("Очередь работает только с целыми числами")
        self.data.append(x)

    def dequeue(self) -> int:
        if not self.data:
            raise IndexError("Очередь пуста")
        return self.data.pop(0)

    def front(self) -> int:
        if not self.data:
            raise IndexError("Очередь пуста")
        return self.data[0]

    def is_empty(self) -> bool:
        return not self.data

    def __len__(self) -> int:
        return len(self.data)
