class Stack:
    def __init__(self) -> None:
        self.data: list[int] = []

    def push(self, x: int) -> None:
        if type(x) is not int:
            raise ValueError("Стек работает только с целыми числами")
        self.data.append(x)

    def pop(self) -> int:
        if not self.data:
            raise IndexError("Стек пуст")
        return self.data.pop()

    def peek(self) -> int:
        if not self.data:
            raise IndexError("Стек пуст")
        return self.data[-1]

    def is_empty(self) -> bool:
        if not self.data:
            return True
        return False

    def __len__(self):
        return len(self.data)

    def min(self) -> int:
        if not self.data:
            raise IndexError("Стек пуст")
        return min(self.data)
