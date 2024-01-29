from collection import Queue
from collection import Deque


def second_lowest_iterative(q: Queue)-> object:
    if q.is_empty():
        print("Queue is empty")
        return
    if q.size() == 1:
        print("Queue has only one element")
        return
    minimum, second_min = q.dequeue(), None
    q.enqueue(minimum)
    for _ in range(q.size() - 1):
        el = q.dequeue()
        if el < minimum:
            second_min = minimum
            minimum = el
        elif el < second_min:
            second_min = el
        q.enqueue(el)
    return second_min


def second_lowest_recursive(q: Queue)-> object:
    if q.is_empty():
        print("Queue is empty")
        return
    if q.size() == 1:
        print("Queue has only one element")
        return
    minimum, second_min = q.dequeue(), None
    q.enqueue(minimum)
    def helper(q: Queue, minimum_rec: object, second_min_rec: object)-> object:
        if q.is_empty():
            return second_min_rec
        el = q.dequeue()
        if el < minimum_rec:
            second_min_rec = minimum_rec
            minimum_rec = el
        elif el < second_min_rec:
            second_min_rec = el
        q.enqueue(el)
        return helper(q, minimum_rec, second_min_rec)
    return helper(q, minimum, second_min)

def merge_sorted_deques_iterative(d1: Deque, d2: Deque):
    if d1.is_empty() and d2.is_empty():
        print("EMPTY deques")
        return
    if d1.is_empty():
        return d2
    if d2.is_empty():
        return d1
    new_deque = Deque()
    while not d1.is_empty() and not d2.is_empty():
        if d1.front() < d2.front():
            new_deque.enqueue(d1.dequeue())
        else:
            new_deque.enqueue(d2.dequeue())
    while not d1.is_empty():
        new_deque.enqueue(d1.dequeue())
    while not d2.is_empty():
        new_deque.enqueue(d2.dequeue())
    return new_deque


def merge_sorted_deques_recursive(d1: Deque, d2: Deque):
    if d1.is_empty() and d2.is_empty():
        print("Empty Deques")
        return
    if d1.is_empty():
        return d2
    if d2.is_empty():
        return d1
    #  Էս մեկը պտի խոստովանեմ որ copilot նա ֆուլլ օգնել ու համարյա չեմ հասկացել,
    #  կուզեի վրայով օֆիսին անպայման անցնել
    def helper(d1: Deque, d2: Deque, new_deque: Deque) -> Deque:
        if d1.is_empty() and d2.is_empty():
            return new_deque
        if d1.is_empty():
            new_deque.enqueue(d2.dequeue())
        elif d2.is_empty():
            new_deque.enqueue(d1.dequeue())
        elif d1.front() < d2.front():
            new_deque.enqueue(d1.dequeue())
        else:
            new_deque.enqueue(d2.dequeue())
        return helper(d1, d2, new_deque)
    return helper(d1, d2, Deque())


class step_iterator:
    def __init__(self, d: Deque, step: int):
        self.__d = d
        self.step = step
        self.__index = 0

    def __next__(self):
        if self.__index >= self.__d.size():
            raise StopIteration
        dequed = []
        for _ in range(self.__index + self.step - 1):
            dequed.append(self.__d.dequeue())
        returnable = self.__d.front()
        for i in range(self.__index + self.step - 1):
            self.__d.enqueue(dequed[i])
        self.__index += self.step
        return returnable

    def __iter__(self):
        return self


def subsequences(sequence: list):
    for i in range(0, 2 ** len(sequence)):
        for j in range(len(sequence)):
            # ոնց կարա մտքովդ անցնի ու սենց բան գրես՞
            # բնականաբար ինտերնետի ուժերով ա գրված
            if i & (1 << j):
                print(sequence[j], end='')
        print()

print("TESSTTT")
subsequences(['A', 'B', 'C', 'D'])