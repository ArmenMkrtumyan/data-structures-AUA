from collection import Stack
from single_linked_list import Node


class myStack(Stack):
    def __init__(self):
        self.__head = None
        self.__len = 0

    def size(self) -> int:
        return self.__len

    def is_empty(self) -> bool:
        return self.__len == 0

    def empty(self) -> None:
        self.__head = None
        self.__len = 0

    def push(self, e: object) -> None:
        node = Node(e, self.__head)
        node.set_head(self.__head)
        self.__head = node
        self.__len += 1

    def pop(self) -> object:
        if self.is_empty():
            print("Stack is empty")
            return
        temp = self.__head
        self.__head = Node.get_head(self.__head)
        self.__len -= 1
        temp.set_head(None)
        return Node.get_value(temp)

    def top(self) -> object:
        if self.is_empty():
            print("Stack is empty")
            return
        return Node.get_value(self.__head)

    def print(self) -> None:
        print(self)

    def __str__(self):
        new_str = ''
        temp = self.__head
        while temp is not None:
            new_str += "|" + str(Node.get_value(temp)) + '|' + '\n'
            temp = Node.get_head(temp)
        return new_str

    def get_top_element(self):
        return self.__head
