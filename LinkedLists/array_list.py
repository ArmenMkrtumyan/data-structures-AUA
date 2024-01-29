from collection import List


class ArrayList(List):
    def __init__(self, capacity: int = 10):
        self.__array = [None] * capacity
        self.__len = 0
        self.__initial_capacity = capacity
        self.__allocated_size = capacity

    def get_allocated_size(self) -> int:
        return self.__allocated_size

    def size(self) -> int:
        return self.__len

    def __resize(self) -> None:
        if self.__len < len(self.__array):
            return
        new_array = [None] * (len(self.__array) * 2)
        for i in range(self.__len):
            new_array[i] = self.__array[i]
        self.__array = new_array
        self.__allocated_size = len(self.__array)

    def is_empty(self) -> bool:
        return self.__len == 0

    def empty(self) -> None:
        self.__array = [None] * self.__initial_capacity
        self.__len = 0

    def first(self) -> object:
        if self.is_empty():
            print("ArrayList is empty")
            return
        return self.__array[0]

    def last(self) -> object:
        if self.is_empty():
            print(ValueError("ArrayList is empty"))
            return
        return self.__array[self.__len - 1]

    def add_first(self, el: object) -> bool:
        self.__resize()
        for i in range(self.__len, 0, -1):
            self.__array[i] = self.__array[i - 1]
        self.__array[0] = el
        self.__len += 1
        return True

    def remove_first(self) -> bool:
        if self.is_empty():
            print("ArrayList is empty")
            return False
        for i in range(0, self.__len - 1):
            self.__array[i] = self.__array[i + 1]
        self.__array[self.__len - 1] = None
        self.__len -= 1
        return True

    def add_last(self, el):
        """
        :param el: object
        :return: bool
        """
        self.__resize()
        self.__array[self.__len] = el
        self.__len += 1
        return True

    def remove_last(self) -> bool:
        if self.is_empty():
            print("ArrayList is empty")
            return False
        self.__array[self.__len - 1] = None
        self.__len -= 1
        return True

    def replace(self, e, r) -> bool:
        """
        :param e: object
        :param r: object
        :return: bool
        """
        for i in range(self.__len):
            if self.__array[i] == e:
                # After few minutes of googling about this warning
                # I've found out that this is just  Bug in PyCharm, fun!
                # the previous one add_last got fixed by just adding docstring
                # Not this one though
                self.__array[i] = r
                return True
        print("Element not found")
        return False

    def add_at(self, e: object, index: int) -> bool:
        if index < 0 or index > self.__len:
            print("Index out of range")
            return False
        self.__resize()
        for i in range(self.__len, -1, -1):
            if i == index:
                # AGAINNNN
                self.__array[i] = e
                self.__len += 1
                return True
            self.__array[i] = self.__array[i - 1]

    def get_at(self, index: int) -> object:
        if index < 0 or index > self.__len:
            print("Index out of range")
            return
        return self.__array[index]

    def print(self) -> None:
        print(self.__array)

    def __str__(self) -> str:
        if self.is_empty():
            return "[]"
        temp = "["
        for i in self.__array:
            if i is None:
                break
            temp += str(i) + ", "
        temp = temp[:-2] + "]"  # remove the last comma and space
        return temp
