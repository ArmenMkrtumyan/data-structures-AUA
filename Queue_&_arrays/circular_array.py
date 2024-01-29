from collection import Deque

class CircularArray(Deque):
    """Dynamic sized Circular array."""

    def __init__(self, capacity=10):
        self._array = [None] * capacity
        self._size = 0
        self._initial_capacity = capacity
        self._start_index = 0

    def empty(self) -> None:
        self._array = [None] * self._initial_capacity
        self._size = 0
        self._start_index = 0

    def size(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    def __str__(self):
        my_str = ""
        for i in range(self._size):
            my_str += str(self._array[i]) + " -> "
        my_str = my_str[:-4]
        return my_str

    def print(self) -> None:
        print(self)

    def _resize(self) -> None:
        if self._size < len(self._array):
            return
        new_array = [None] * (len(self._array) * 2)
        for i in range(self._size):
            # Այո սա գողացել եմ մեր սլայդներից, շատ լավ էր է գրած
            new_array[i] = self._array[(self._start_index + i) % len(self._array)]
        self._start_index = 0
        self._array = new_array

    def enqueue(self, e: object) -> None:
        self._resize()
        # Wrong again pyCharm?
        self._array[(self._start_index - 1) % len(self._array)] = e
        self._start_index = (self._start_index - 1) % len(self._array)
        self._size += 1

    def dequeue(self) -> object:
        if self.is_empty():
            raise ValueError("Circular array is empty")
        self._resize()
        last = self._array[(self._start_index + self._size - 1) % len(self._array)]
        self._array[(self._start_index + self._size - 1) % len(self._array)] = None
        self._size -= 1
        return last

    def front(self) -> object:
        if self.is_empty():
            raise ValueError("Circular array is empty")
        return self._array[(self._start_index + self._size - 1) % len(self._array)]

    def back(self) -> object:
        if self.is_empty():
            raise ValueError("Circular array is empty")
        return self._array[self._start_index % len(self._array)]

    # swaps the first occurrence of v1 in deque with
    # the first occurrence of v2
    def swap(self, v1: object, v2: object) -> None:
        index_1 = -1
        index_2 = -1
        print("Self size is ", self._size)
        for i in range(self._size):
            print(f"i is {i}, index_1 is {index_1} index_2 is: {index_2}")
            if self._array[i] == v1 and index_1 == -1:
                index_1 = i
            if self._array[i] == v2 and index_2 == -1:
                index_2 = i
        if index_1 == -1 or index_2 == -1:
            print("Not found ")
            return
        self._array[index_1], self._array[index_2] = v2, v1

    def left_enqueue(self, e: object) -> None:
        self._resize()
        self._array[(self._start_index + self._size - 1) % len(self._array)] = e
        self._start_index = (self._start_index + self._size - 1) % len(self._array)
        self._size += 1

    def right_dequeue(self) -> object:
        if self.is_empty():
            raise ValueError("Circular array is empty")
        self._resize()
        last = self._array[self._start_index % len(self._array)]
        self._array[self._start_index % len(self._array)] = None
        self._start_index = (self._start_index + 1) % len(self._array)
        self._size -= 1
        return last

