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

class Stack(Collection):
    @abstractmethod
    def push(self, e: object) -> None:
        pass

    @abstractmethod
    def pop(self) -> object:
        pass

    @abstractmethod
    def top(self) -> object:
        pass


class my_set(Collection):
    @abstractmethod
    def add(self, value: object) -> bool:
        pass

    @abstractmethod
    def remove(self, value: object) -> bool:
        pass

    @abstractmethod
    def contains(self, value: object) -> bool:
        pass

    @abstractmethod
    def equals(self, s: "Set class") -> bool:
        pass

    @abstractmethod
    def remove_element_at(self, index: int) -> object:  # iterate horizontally
        pass


class Map(Collection):
    def put(self, key: object, value: object) -> "Object(value)":
        pass

    def get(self, key: object) -> "Object(value)":
        pass

    def remove(self, key: object) -> "Object(value)":
        pass

    def keySet(self) -> " a HashSet of all keys in the map":
        pass

class List(Collection):
    @abstractmethod
    def add_first(self, e: object) -> None:
        pass

    @abstractmethod
    def add_last(self, e: object) -> None:
        pass

    @abstractmethod
    def remove_first(self) -> bool:
        pass

    @abstractmethod
    def remove_last(self) -> bool:
        pass

    @abstractmethod
    def first(self) -> object:
        pass

    @abstractmethod
    def last(self) -> object:
        pass

    @abstractmethod
    def replace(self, e: object, r: object) -> bool:
        pass

    @abstractmethod
    def add_at(self, e: object, index: int) -> bool:
        pass

    @abstractmethod
    def get_at(self, index: int) -> object:
        pass
