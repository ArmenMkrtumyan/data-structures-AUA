from my_collections import my_set

class StepIterator:
    def __init__(self, hash_table, length, step = 1):
        self.step = step
        self.hash_table = hash_table
        self.current_step = 0
        self.len = length
        print(self.len)

    def __next__(self):
        if self.current_step >= self.len:
            raise StopIteration
        current = 0
        # print(self.hash_table)
        for i in self.hash_table:
            if i:
                tmp = i
                while tmp:
                    # print(f"tmp data: {tmp.data}, current step: {self.current_step}, current: {current}")
                    if current == self.current_step:
                        self.current_step += self.step
                        return tmp.data
                    tmp = tmp.next
                    if tmp:
                        current += 1
                current += 1

class HashSet(my_set):
    _MAX_HASH = 26

    def __init__(self):
        self._hash_table = [None] * HashSet._MAX_HASH
        self._size = 0

    class Node:
        def __init__(self, d, n=None):
            self.data = d
            self.next = n

    def hash(self, e):
        x = ord(str(e[0]).lower()) - ord("k")
        return x

    def add(self, element):
        ind = self.hash(element)
        temp = self._hash_table[ind]
        
        if temp is None:
            temp = self.Node(element)
            self._hash_table[ind] = temp
            self._size += 1
            return True
    
        while temp.next is not None:
            if temp.data == element:
                return False
            temp = temp.next
        if temp.data == element:
            return False
        temp.next = self.Node(element)
        self._size += 1
        return True

    def remove(self, element):
        ind = self.hash(element)
        temp = self._hash_table[ind]

        if temp.data == element:
            temp.data = None
            self.size -= 1
            return False
        while temp.next:
            if temp.next.data == element:
                temp.next = temp.next.next
                self._size -= 1
                return True
            temp = temp.next
        return False

    def print(self) -> None:
        print(self)

    def __str__(self):
        my_string = ""
        for i in range (self._MAX_HASH):
            if self._hash_table[i] is not None:
                tmp = self._hash_table[i]
                my_string += str(i) + ": "
                while tmp:
                    my_string += " ->" + tmp.data
                    tmp = tmp.next
                my_string += "\n"
        return my_string

    def size(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    def empty(self) -> None:
        self._hash_table = [None] * HashSet._MAX_HASH
        self._size = 0

    def contains(self, value: object) -> bool:
        ind = self.hash(value)
        temp = self._hash_table[ind]
        
        if temp is None:
            return False
        while temp:
            if temp.data == value:
                return True
            temp = temp.next
        return False
    
    def equals(self, s: "Set class") -> bool:
        for i in s:
            if i not in self._hash_table:
                return False
            else:
                if len(self._hash_table[i]) != len(s._hash_table[i]):
                    return False
                else:
                    tmp = self._hash_table[i]
                    tmp2 = s._hash_table[i]
                    while tmp:
                        while tmp2:
                            if tmp.data == tmp2.data:
                                return False
                            tmp2 = tmp2.next
                        tmp = tmp.next
        return True

    def remove_element_at(self, index: int) -> object:  # iterate horizontally
        counter = 0
        for i in range(HashSet._MAX_HASH):
            tmp = self._hash_table[i]
            while tmp:
                if counter + 1 == index:
                    data = tmp.next.data
                    tmp.next = tmp.next.next
                    return data
                tmp = tmp.next
                counter += 1
        return None

    def remove_after(self, el) -> object:
        for i in range(HashSet._MAX_HASH):
            tmp = self._hash_table[i]
            if not tmp:
                continue
            while tmp.next:
                if tmp.data == el:
                    returnable = tmp.next.data
                    tmp.next = tmp.next.next
                    self._size -= 1
                    return returnable
                tmp = tmp.next
            if tmp.data == el:
                returnable = tmp.data
                tmp = None
                self._hash_table[i] = None
                self._size -= 1
                return returnable
        return None


    def __iter__(self):
        my_iterator = StepIterator(self._hash_table, self._size)
        return my_iterator

    def hash_set_iterator(self, step):
        my_iterator = StepIterator(self._hash_table, self._size, step)
        return my_iterator