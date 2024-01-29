from collection import List


class DoubleLinkedList(List):
    class Node:
        def __init__(self, value, _next: object = None, _prev: object = None):
            self._value = value
            self._next = _next
            self._prev = _prev

        def get_value(self):
            return self._value

        def get_next(self):
            return self._next

        def get_prev(self):
            return self._prev

        def set_value(self, value: object):
            self._value = value

        def set_next(self, _next: object):
            self._next = _next

        def set_prev(self, _prev: object):
            self._prev = _prev

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__len = 0

    def first(self) -> object:
        return self.Node.get_value(self.__tail)

    def last(self) -> object:
        temp = self.__tail
        while self.Node.get_next(temp) is not None:
            temp = self.Node.get_next(temp)
        return self.Node.get_value(temp)

    def get_at(self, index: int) -> object:
        starting_address = self.__tail
        for i in range(0, index):
            if self.Node.get_next(starting_address) is None:
                print("Index out of range")
                return
            starting_address = self.Node.get_next(starting_address)
        return self.Node.get_value(starting_address)

    def print(self) -> None:
        print(self)

    def __str__(self) -> str:
        new_str = ''
        for i in range(0, self.__len):
            new_str += str(self.get_at(i)) + ' <-> '
        new_str += 'None'

        return new_str

    def size(self) -> int:
        return self.__len

    def is_empty(self) -> bool:
        return self.__len == 0

    def add_first(self, e: object) -> None:
        if self.__len == 0:
            self.__tail = self.__head = self.Node(e)
            self.__len += 1
            return
        node = self.Node(e, self.__tail, None)
        self.Node.set_prev(self.__tail, node)
        self.__tail = node
        self.__len += 1

    def empty(self) -> None:
        self.__tail = None
        self.__head = None
        self.__len = 0

    def add_last(self, e: object) -> None:
        node = self.Node(e, None, self.__head)
        if self.__len == 0:
            self.__tail = self.__head = node
        else:
            temp = self.__tail
            while self.Node.get_next(temp) is not None:
                temp = self.Node.get_next(temp)
            self.Node.set_next(temp, node)
            self.Node.set_prev(node, temp)
        self.__len += 1

    def remove_first(self) -> bool:
        if self.__len == 0:
            print("List is empty")
            return False
        self.__tail = self.Node.get_next(self.__tail)
        self.__len -= 1

        return True

    def remove_last(self) -> bool:
        if self.__len == 0:
            print("List is empty")
            return False
        temp = self.__tail
        i = 0
        while i < self.__len - 1:
            temp = self.Node.get_next(temp)
            i += 1
        self.Node.set_next(temp, None)
        self.__head = temp
        self.__len -= 1
        return True

    def replace(self, e: object, r: object) -> bool:
        temp = self.__tail
        for i in range(0, self.__len):
            if self.Node.get_value(temp) == e:
                self.Node.set_value(temp, r)
                return True
            temp = self.Node.get_next(temp)
        print("Element not found")
        return False

    def add_at(self, e: object, index: int) -> bool:
        if index < 0:
            print("Index out of range")
            return False
        temp = self.__tail
        for i in range(0, index - 1):
            if self.Node.get_next(temp) is None:
                print("Index out of range")
                return False
            temp = self.Node.get_next(temp)
        node = self.Node(e, self.Node.get_next(temp), self.Node.get_prev(temp))
        self.Node.set_next(temp, node)
        self.__len += 1
        return True
