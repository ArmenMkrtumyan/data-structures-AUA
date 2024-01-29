from abc import ABC, abstractmethod


class Collection(ABC):
    """
        The ‘abc’ module in the Python library provides the infrastructure for defining custom abstract base classes.
        Abstract class cannot be instantiated in python. An Abstract method can be call by its subclasses.
    """
    @abstractmethod
    def print(self) -> None:
        pass

    @abstractmethod
    def size(self) -> int:
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        pass

    @abstractmethod
    def empty(self) -> None:
        pass


class Queue(Collection):
    @abstractmethod
    def enqueue(self, e: object) -> None:
        pass

    @abstractmethod
    def dequeue(self) -> object:
        pass

    @abstractmethod
    def front(self) -> object:
        pass

    @abstractmethod
    def back(self) -> object:
        pass

    # swaps the first occurrence of v1 in deque with
    # the first occurrence of v2
    @abstractmethod
    def swap(self, v1: object, v2: object) -> None:
        pass


class Deque(Queue):
    @abstractmethod
    def left_enqueue(self, e: object) -> None:
        pass

    @abstractmethod
    def right_dequeue(self) -> object:
        pass