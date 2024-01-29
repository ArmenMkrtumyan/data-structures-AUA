from collection import Deque

'''
implement DoubleLinkedListDeque class which implements the Deque
interface(abstraction) using a double linked list
'''


class Node:
    def __init__(self, value, tail=None):
        self.next = tail
        self.value = value


class DoubleLinkedListDeque(Deque):
    def __init__(self, maxsize=10):
        self.maxsize: int = maxsize
        self.tail: "object of type Node" = None
        self.head: "object of type Node" = None
        self.current_size: int = 0

    def size(self) -> int:
        return self.current_size

    def enqueue(self, e: object) -> None:
        node = Node(e, None)
        print(self)
        if self.head == self.tail is None:
            self.tail = node
            self.head = node
        else:
            self.tail.next = node
            self.tail = node
        self.current_size += 1

    def dequeue(self) -> object:
        last = None
        if self.current_size == 0:
            print("Queue is empty")
        if self.current_size == 1:
            first = self.tail.value
            self.tail = None
            self.current_size = 0
            self.head = None
        else:
            first = self.head
            self.head = self.head.next
            self.current_size -= 1
        return first.value

    def left_enqueue(self, e: object) -> None:
        if self.head == self.tail is None:
            node = Node(e)
            self.tail = node
            self.head = node
        else:
            node = Node(e, self.head)
            self.head = node

        self.current_size += 1

    def right_dequeue(self) -> object:
        last = None
        if self.current_size == 0:
            print("Queue is empty")
        if self.current_size == 1:
            last = self.tail.value
            self.tail = None
            self.current_size = 0
            self.head = None
        else:
            tmp = self.head
            # Dumb warning
            while tmp.next.next is not None:
                tmp = tmp.next
            last = tmp.next.value
            tmp.next = None
            self.tail = tmp
            self.current_size -= 1
        return last

    def front(self) -> object:
        if self.empty():
            raise ValueError("Queue is empty")
        return self.head.value

    def back(self) -> object:
        if self.empty():
            raise ValueError("Queue is empty")
        return self.tail.value

    # swaps the first occurrence of v1 in deque with
    # the first occurrence of v2
    def swap(self, v1: object, v2: object) -> None:
        tmp_1 = self.head
        tmp_1_index = -1
        tmp_2 = self.head
        tmp_2_index = -1
        i = 0
        while i < self.current_size:
            if tmp_1.next.value == v1 and tmp_1_index != -1:
                tmp_1.next.value = v2
                tmp_1_index = i
            if tmp_2.next.value == v2 and tmp_1_index != -1:
                tmp_2.next.value = v1
                tmp_2_index = i

    def maxsize(self) -> int:
        return self.maxsize

    def __str__(self):
        my_str = ""
        tmp = self.head
        for i in range(self.current_size):
            # Gives a warning but works
            my_str += str(tmp.value) + " -> "
            tmp = tmp.next
        my_str = my_str[:-4]
        return my_str

    def print(self):
        return self.__str__()

    def is_empty(self) -> bool:
        return self.current_size == 0

    def empty(self) -> None:
        self.tail = None
        self.head = None
        self.current_size = 0

    # def full(self) -> bool:
    #     return self.current_size == self.maxsize
    #

    # def get(self) -> object:
    #     if self.empty():
    #         print("Queue is empty")
    #         return
    #     return self.__remove_last()
    #

    # def reverse_que(self):
    #     if self.empty():
    #         return
    #     tmp = self.__remove_last()
    #     print(tmp, end = " - ")
    #     self.reverse_que()
    #     self.put(tmp)
    #     print(f"UPDATED SELF IS: {self}")
    #

    """ 
    Implement a reverse iterator for ArrayQueue class which iterates over the queue elements 
    starting from last element and goes up till first element.
    """
    def __iter__(self):
        return self
    def reverse_iterator(self):
        if self.empty():
            return
        tmp = self.right_dequeue()
        print(tmp, end=" - ")
        self.reverse_iterator()
        self.left_enqueue(tmp)
        print(f"UPDATED SELF IS: {self}")
