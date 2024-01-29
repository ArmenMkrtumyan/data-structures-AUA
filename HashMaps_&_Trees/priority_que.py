from collection import PriorityQueue
from university_management import Student

class MaxPriorityQueue(PriorityQueue):
    def __init__(self):
        self._array = []

    def size(self) -> int:
        return len(self._array)

    def is_empty(self) -> bool:
        return len(self._array) == 0

    def empty(self):
        self._array = []

    def __str__(self):
        return ", ".join([str(i) for i in self._array])

    def add(self, el):
        return self.enqueue(el)

    def remove(self, el):
        return self.dequeue(el)

    def has(self, el):
        return el in self._array

    def print(self) -> None:
        print(self._array)

    def first(self):
        return self._array[0]

    def enqueue(self, el):
        self._array.append(el)

        # Execute float up operation
        i = len(self._array) - 1
        p = (i - 1) // 2

        while p >= 0 and self._array[i] > self._array[p]:
            # swap values
            self._array[i], self._array[p] = self._array[p], self._array[i]
            i = p
            p = (p - 1) // 2

    def dequeue(self):
        if len(self._array) == 0:
            return None

        max_value = self._array[0]

        # replace with last value
        self._array[0] = self._array[len(self._array) - 1]
        # remove last value
        self._array.pop()

        # Execute Float Down operation
        i = 0
        while i < len(self._array):
            max_index = i
            left = 2 * i + 1
            right = 2 * i + 2
            if left < len(self._array) and self._array[left] > self._array[max_index]:
                max_index = left
            if right < len(self._array) and self._array[right] > self._array[max_index]:
                max_index = right
            if max_index == i:
                break

            # swap the value
            self._array[i], self._array[max_index] = (
                self._array[max_index],
                self._array[i],
            )
            i = max_index

        return max_value

class InorderIterator:
    def __init__(self, array):
        self.queue = array
        self.current = 0

    def __next__(self):
        if self.current == len(self.queue):
            raise StopIteration
        self.current += 1
        return self.queue[self.current - 1]

    def __iter__(self):
        return self

class MinPriorityQueue(PriorityQueue):

    def __init__(self):
        self._array = []

    def size(self) -> int:
        return len(self._array)

    def is_empty(self) -> bool:
        return len(self._array) == 0

    def empty(self):
        self._array = []

    def __str__(self):
        return ", ".join([i._name for i in self._array])

    def add(self, el):
        return self.enqueue(el)

    def remove(self, el):
        return self.dequeue(el)

    def has(self, el):
        return el in self._array

    def print(self) -> None:
        print(self._array)

    def first(self):
        return self._array[0]

    def enqueue(self, el):
        self._array.append(el)

        # Execute float up operation
        i = len(self._array) - 1
        p = (i - 1) // 2

        while p >= 0 and self._array[i] < self._array[p]:
            # swap values
            self._array[i], self._array[p] = self._array[p], self._array[i]
            i = p
            p = (p - 1) // 2

    def dequeue(self):
        if len(self._array) == 0:
            return None

        min_value = self._array[0]

        # replace with last value
        self._array[0] = self._array[len(self._array) - 1]
        # remove last value
        self._array.pop()

        # Execute Float Down operation
        i = 0
        while i < len(self._array):
            min_index = i
            left = 2 * i + 1
            right = 2 * i + 2
            if left < len(self._array) and self._array[left] < self._array[min_index]:
                min_index = left
            if right < len(self._array) and self._array[right] < self._array[min_index]:
                min_index = right
            if min_index == i:
                break

            # swap the value
            self._array[i], self._array[min_index] = (
                self._array[min_index],
                self._array[i],
            )
            i = min_index

        return min_value

    def _students_queue(self, student: Student):
        self.enqueue(student)

    def _deque_student(self, student: Student):
        self.dequeue(student)

    def __iter__(self):
        my_iterator = InorderIterator(self._array)
        return my_iterator

    def __next__(self):
        return next(self.__iter__())
