import single_linked_list
import double_linked_list
import array_list
import stack
import iterators
import recursive_checkers


def LinkedLists(list_type):
    print("TYPE IS: ", type(list_type))
    my_list = list_type
    my_list.add_last(1)
    my_list.add_last(3)
    my_list.add_first(8)
    my_list.add_last(3)
    my_list.add_first(8)
    my_list.remove_first()
    my_list.remove_last()
    print(my_list)
    print("Size is: " + str(my_list.size()))
    print("First element is: " + str(my_list.first()))
    print("Last element is: " + str(my_list.last()))
    element = 1
    if my_list.get_at(element):
        print(f"Getting element at {element}: " + str(my_list.get_at(element)))
    print("Replacing the first element by the value of second")
    my_list.replace(my_list.get_at(1), my_list.get_at(2))
    print(my_list)
    print("Adding an element 4 at 1")
    my_list.add_at(4, 1)
    print(my_list)
    print("Empty?: ", my_list.is_empty())
    print("Emptying the list")
    my_list.empty()
    print("Empty?: ", my_list.is_empty())


def ArrayList(my_array_list):
    print("TYPE IS: ", type(my_array_list))
    print(my_array_list)
    print("Size of my array list is: " + str(my_array_list.size()))
    print("Adding 11 1's to the array list")
    for i in range(11):
        my_array_list.add_first(1)
    print(my_array_list)
    print("As we can see it prints out the elements of the aray list, whereas its actual")
    print("Allocated size is: " + str(my_array_list.get_allocated_size()))
    print("Empty?: ", my_array_list.is_empty())
    print("Lets remove few (3) elements")
    for i in range(3):
        my_array_list.remove_first()
    print(my_array_list)
    print("Size of my array list is: " + str(my_array_list.size()))
    print("Emptying the array list")
    my_array_list.empty()
    print("Empty?: ", my_array_list.is_empty())
    print(my_array_list)


def Stacks(my_stack):
    print("TYPE IS: ", type(my_stack))
    print("Empty?: ", my_stack.is_empty())
    print("Pushing 5 elements to the stack")
    for i in range(5):
        my_stack.push(i)
    print(my_stack)
    print("Size of the stack is: " + str(my_stack.size()))
    print("Empty?: ", my_stack.is_empty())
    print("Popping 2 elements from the stack")
    for i in range(2):
        my_stack.pop()
    print(my_stack)
    print("As we can see, the top elements of the stack were removed")
    print("Size of the stack is: " + str(my_stack.size()))
    print("Emptying the stack")
    my_stack.empty()
    print("Empty?: ", my_stack.is_empty())
    print(my_stack)


# Ex 3
# single linked list

# list_type_1 = single_linked_list.LinkedList()
# LinkedLists(list_type_1)

# Ex 4
# double linked list

# list_type_2 = double_linked_list.DoubleLinkedList()
# LinkedLists(list_type_2)

# Ex 5
# array list

# array_list_1 = array_list.ArrayList()
# ArrayList(array_list_1)

# Ex 6
# stack

# stack_1 = stack.myStack()
# Stacks(stack_1)

# Ex 7
# linked list forward iterator

# list_type_1 = single_linked_list.LinkedList()
# print("\nSample single linked list\n")
# for i in range(5):
#     list_type_1.add_last(i)
# print(list_type_1)
#
# print("\nLinked list forward iterator\n")
# iterator_1 = iterators.LinkedListForwardIterator(list_type_1.get_tail())
#
# while True:
#     try:
#         print(next(iterator_1))
#     except StopIteration:
#         break

# stack iterator

# stack_1 = stack.myStack()
# print("\nSample stack\n")
# for i in range(4, 10):
#     stack_1.push(i)
# print(stack_1)
#
# iterator_1 = iterators.StackIterator(stack_1.get_top_element())
# print("\nStack iterator\n")
# while True:
#     try:
#         print(next(iterator_1))
#     except StopIteration:
#         break

# Ex 8
# Linked list odd positions iterator

# linked_list = single_linked_list.LinkedList()
# for i in range(10,20):
#     linked_list.add_last(i)
# print("Sample linked list")
# print(linked_list)
#
# print("Iterator for odd positions")
# odd_iterator = iterators.oodPositionIterator(linked_list.get_tail())
# while True:
#     try:
#         element = next(odd_iterator)
#         if element is not None:
#             print(element)
#     except StopIteration:
#         break

# Ex 9
# reverse LinkedList

linked_list = single_linked_list.LinkedList()
for i in range(40, 50):
    linked_list.add_first(i)
print("Sample linked list")
print(linked_list)
linked_list.reverse()
print(linked_list)
print(linked_list.first())
print(linked_list.get_tail().get_value())
# Ex 10
# reverse List

# linked_list = single_linked_list.LinkedList()
# for i in range(40, 50):
#     linked_list.add_first(i)
# print("Sample linked list")
# print(linked_list)
# print("Reversing the single linked list")
# recursive_checkers.reverse(linked_list)
# print(linked_list)
#
# double_linked_list_1 = double_linked_list.DoubleLinkedList()
# for i in range(40, 50):
#     double_linked_list_1.add_first(i)
# print("Sample double linked list")
# print(double_linked_list_1)
# print("Reverse double linked list")
# recursive_checkers.reverse(double_linked_list_1)
# print(double_linked_list_1)

# 11
# recursive stack

# stack_1 = stack.myStack()
# for i in range(4, 10):
#     stack_1.push(i)
# print("Sample stack")
# print(stack_1)
#
# element = 5
# print(f"Sample stack contains element {element} ?: {recursive_checkers.contains(element, stack_1)}")
# print("As you can see, the stack is untouched")
# print(stack_1)

# Ex 12
# iterative add_before

# linked_list = single_linked_list.LinkedList()
# for i in range(80, 90):
#     linked_list.add_last(i)
# print("Sample linked list")
# print(linked_list)
#
# print("Adding 100 before 81")
# linked_list.iterative_add_before(81, 100)
# print(linked_list)

# recursive add_before

# linked_list = single_linked_list.LinkedList()
# for i in range(80, 90):
#     linked_list.add_last(i)
# print("Sample linked list")
# print(linked_list)
# print("Adding 100 before 80")
# linked_list.recursive_add_before(89, 100)
# print(linked_list)

# Ex 13

# iterative add_after

# linked_list = single_linked_list.LinkedList()
# for i in range(100, 110):
#     linked_list.add_last(i)
# print("Sample linked list")
# print(linked_list)
#
# print("Adding 100 before 81")
# linked_list.iterative_add_after(109, 999)
# print(linked_list)

# recursive add_after

# linked_list = single_linked_list.LinkedList()
# for i in range(20, 30):
#     linked_list.add_last(i)
# print("Sample linked list")
# print(linked_list)
# print("Adding 100 before 80")
# if linked_list.recursive_add_after(29, 999) is None:
#     print("Element not found")
# print(linked_list)
