from collection import List


class Node:
    def __init__(self, value, head: object = None):
        self._value = value
        self._head = head

    def get_value(self):
        return self._value

    def get_head(self):
        return self._head

    def set_value(self, value: object):
        self._value = value

    def set_head(self, head: object):
        self._head = head


class LinkedList(List):
    def __init__(self):
        self.__tail = None
        self.__len = 0

    def first(self) -> object:
        if self.__len == 0:
            print("List is empty")
            return
        return self.__tail.get_value()

    def last(self) -> object:
        if self.__len == 0:
            print("List is empty")
            return
        temp = self.__tail
        while temp.get_head() is not None:
            temp = temp.get_head()
        return temp.get_value()

    def get_at(self, index: int) -> object:
        starting_address = self.__tail
        for i in range(0, index):
            if starting_address.get_head() is None:
                print("Index out of range")
                return
            starting_address = starting_address.get_head()
        return starting_address.get_value()

    def print(self) -> None:
        print(self)

    def __str__(self) -> str:
        new_str = ''
        for i in range(0, self.__len):
            new_str += str(self.get_at(i)) + ' -> '
        new_str += 'None'
        return new_str

    def size(self) -> int:
        return self.__len

    def is_empty(self) -> bool:
        return self.__len == 0

    def add_first(self, e: object) -> None:
        node = Node(e, None)
        Node.set_head(node, self.__tail)
        self.__tail = node
        self.__len += 1

    def empty(self) -> None:
        self.__tail = None
        self.__len = 0

    def add_last(self, e: object) -> None:
        node = Node(e, None)
        if self.__len == 0:
            self.__tail = node
        else:
            temp = self.__tail
            while temp.get_head() is not None:
                temp = temp.get_head()
            Node.set_head(temp, node)
        self.__len += 1

    def remove_first(self) -> bool:
        if self.__len == 0:
            print("List is empty")
            return False
        self.__tail = self.__tail.get_head()
        self.__len -= 1
        return True

    def remove_last(self) -> bool:
        if self.__len == 0:
            print("List is empty")
            return False
        temp = self.__tail
        i = 0
        while i < self.__len - 1:
            temp = temp.get_head()
            i += 1
        Node.set_head(temp, None)
        self.__len -= 1
        return True

    def replace(self, e: object, r: object) -> bool:
        temp = self.__tail
        for i in range(0, self.__len):
            if temp.get_value() == e:
                Node.set_value(temp, r)
                return True
            temp = temp.get_head()
        print("Element not found")
        return False

    def add_at(self, e: object, index: int) -> bool:
        if index < 0:
            print("Index out of range")
            return False
        temp = self.__tail
        for i in range(0, index - 1):
            if temp.get_head() is None:
                print("Index out of range")
                return False
            temp = temp.get_head()
        node = Node(e, temp.get_head())
        Node.set_head(temp, node)
        self.__len += 1
        return True

    def get_tail(self) -> Node:
        return self.__tail

    # Ex 9

    @staticmethod
    def _reverse_rec(self, node: Node, k = 0):
        if node.get_head() is None:
            self.add_first(node.get_value())
            for i in range(k+1):
                self.remove_last()
            return
        self.add_first(node.get_value())
        self._reverse_rec(self, node.get_head(), k + 1)

    def reverse(self):
        self._reverse_rec(self, self.__tail)

    # Ex 12

    @staticmethod
    def recursive_before(self, start, el: object):
        if start is None:
            return None
        if start.get_head().get_value() == el:
            return start
        return self.recursive_before(self, start.get_head(), el)

    def recursive_add_before(self, el: object, n: object):
        if self.__len == 0:
            print("List is empty")
            return
        if el is None or n is None:
            print("None is not a valid value")
            return
        if self.__tail.get_value() == el:
            self.add_first(n)
            self.__len += 1
            return
        point = self.recursive_before(self, self.__tail, el)
        if not point:
            return None
        node = Node(n, point.get_head())
        point.set_head(node)
        self.__len += 1

    def iterative_add_before(self, el: object, n: object):
        if self.__len == 0:
            print("List is empty")
        if el is None or n is None:
            print("None is not a valid value")
            return
        else:
            start = self.__tail
            if start.get_value() == el:
                self.add_first(n)
                self.__len += 1
                return
            for i in range(self.__len-1):
                if start.get_head().get_value() == el:
                    node = Node(n, start.get_head())
                    start.set_head(node)
                    self.__len += 1
                    break
                start = start.get_head()
        print(f"Element {el} not found in the list")

    # Ex 13

    def iterative_add_after(self, el: object, n: object):
        if self.__len == 0:
            print("List is empty")
        if el is None or n is None:
            print("None is not a valid value")
            return
        else:
            start = self.__tail
            if start.get_value() == el:
                node = Node(n, start.get_head())
                start.set_head(node)
                self.__len += 1
                return
            for i in range(self.__len-1):
                if start.get_head().get_value() == el:
                    node = Node(n, start.get_head().get_head())
                    start.get_head().set_head(node)
                    self.__len += 1
                    break
                start = start.get_head()
        print(f"Element {el} not found in the list")

    @staticmethod
    def recursive_after(self, start, el: object):
        if start.get_head() is None:
            return None
        if start.get_head().get_value() == el:
            return start
        return self.recursive_after(self, start.get_head(), el)

    def recursive_add_after(self, el: object, n: object):
        if self.__len == 0:
            print("List is empty")
            return
        if el is None or n is None:
            print("None is not a valid value")
            return
        if self.__tail.get_value() == el:
            node = Node(n, self.__tail.get_head())
            self.__tail.set_head(node)
            self.__len += 1
            return
        point = self.recursive_after(self, self.__tail, el)
        if not point:
            return None
        node = Node(n, point.get_head().get_head())
        point.get_head().set_head(node)
        self.__len += 1
