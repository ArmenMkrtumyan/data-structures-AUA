class LinkedListForwardIterator:
    def __init__(self, tail):
        self.tail = tail

    def __next__(self):
        if self.tail is None:
            raise StopIteration
        temp = self.tail
        self.tail = self.tail.get_head()
        return temp.get_value()


class StackIterator:
    def __init__(self, head):
        self.__head = head

    def __next__(self):
        if self.__head is None:
            raise StopIteration
        temp = self.__head
        self.__head = temp.get_head()
        return temp.get_value()


class oodPositionIterator:
    """
    Iterator for odd positions in a linked list
    """

    def __init__(self, tail):
        self.__tail = tail
        self.__count = 0

    def __next__(self):
        if self.__tail is None:
            raise StopIteration
        if self.__count % 2 != 0:
            temp = self.__tail
            self.__tail = self.__tail.get_head()
            self.__count += 1
            return temp.get_value()
        self.__tail = self.__tail.get_head()
        self.__count += 1
        return None
