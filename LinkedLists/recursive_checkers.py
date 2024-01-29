from collection import Stack, List
import stack

# Ex 10


def reverse(l: List):
    if l.size() == 0:
        return
    temp = l.first()
    l.remove_first()
    reverse(l)
    l.add_last(temp)

# Ex 11

def contains(el: object, s: Stack) -> bool:
    if s.is_empty():
        return False
    temp_1 = stack.myStack()
    temp_2 = stack.myStack()
    # we don't wanna to lose s
    for i in range(s.size()):
        temp = s.pop()
        temp_1.push(temp)
        temp_2.push(temp)
    while not temp_1.is_empty():
        if temp_1.pop() == el:
            while not temp_2.is_empty():
                s.push(temp_2.pop())
            return True
    while not temp_2.is_empty():
        s.push(temp_2.pop())
    return False
