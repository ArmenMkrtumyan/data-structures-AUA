from my_collections import Map
from hash_set import HashSet

class hash_iterator:
    def __init__(self, hash_table, length, step = 1):
        self.step = step
        self.hash_table = hash_table
        self.current_step = 0
        self.len = length
        
    def __next__(self):
        if self.current_step >= self.len:
            raise StopIteration
        counter = 0
        for i in self.hash_table:
            if i:
                if counter == self.current_step:
                    tmp = [i._key, i._value]
                    self.current_step += self.step
                    return tmp
            counter += 1

        self.current_step += self.step
        return self.__next__()


class HashMap(Map):
    _MAX_HASH = 10

    def __init__ (self):
        self._hash_table = [None] * HashMap._MAX_HASH
        self._size = 0

    class Entry:
        def __init__(self, k, v, n=None):
            self._key = k
            self._value = v
            self._next = n

        def key (self):
            return self._key

        def value (self):
            return self._value

        def __str__(self):
            return "(" + str(self._key) + "," + self._value + ")"

    def _hash(self, e):
        if e > 50:
            e /= 10
        return e % HashMap._MAX_HASH

    def put(self, k, v):
        ind = self._hash(k)
        temp = self._hash_table[ind]
        while temp:
            if temp._key == k:
                old_value = temp._value
                temp._value = v
                return old_value
            temp = temp._next
        self._hash_table[ind] = HashMap.Entry(k, v, self._hash_table[ind])
        self._size += 1
        return v

    def get(self, k):
        ind = self._hash(k)
        temp = self._hash_table[ind]
        while temp:
            if temp._key == k:
                return temp._value
            temp = temp._next
        return None

    def remove(self, key: object) -> object:
        ind = self._hash(key)
        temp = self._hash_table[ind]
        if temp._key == key:
            self._hash_table[ind] = temp._next
            self._size -= 1
            return temp._value
        while temp._next:
            if temp._next._key == key:
                old_value = temp._next._value
                temp._next = temp._next._next
                self._size -= 1
                return old_value
            temp = temp._next
        return None
        
    def keySet(self) -> " a HashSet of all keys in the map":
        my_set = HashSet()
        for i in self._hash_table:
            if i:
                my_set.add(i._key)
        return my_set
    
    def print(self) -> None:
        print(self)
        
    def __str__(self):
        my_str = ""
        for i in range(len(self._hash_table)):
            my_str += str(i) + ": "
            temp = self._hash_table[i]
            while temp:
                my_str += str(temp) + " -> "
                temp = temp._next
            my_str = my_str[:-4]
            my_str += "\n"
        return my_str
        
    def size(self) -> int:
        return self._size
    
    def is_empty(self) -> bool:
        return self._size == 0
    
    def empty(self) -> None:
        self._hash_table = [None] * HashMap._MAX_HASH
        self._size = 0

    def __iter__(self):
        my_iterator = hash_iterator(self._hash_table, HashMap._MAX_HASH, 1)
        return my_iterator
