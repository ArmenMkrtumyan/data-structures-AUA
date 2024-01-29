"""Test your code."""
from my_collections import SingleLinkedList, DoubleLinkedList, LinkedStack, ArrayList, get_max_element


def create_list(arr, list_class):
    new_list = list_class()
    for e in arr:
        new_list.add_last(e)
    return new_list


def create_stack(arr):
    new_stack = LinkedStack()
    for e in arr:
        new_stack.push(e)
    return new_stack


def test_list_remove_min(task, list_class):
    """This function is for testing Ex1 and Ex2"""
    print("Running task " + str(task) + " tests for remove_min method in " + list_class.__name__)

    print("\t Trying to remove min element from empty list")
    # The expected behaviour is that the size of the list is not changed and the min_value is None
    empty_list = create_list([], list_class)
    s = empty_list.size()
    min_value = empty_list.remove_min()
    # Check min value
    if min_value is None:
        print("\t\t PASS: no element is removed")
    else:
        print("\t\t FAIL: for the empty list min value should be None")
    # Check List size
    if empty_list.size() == s:
        print("\t\t PASS: list size is not changed")
    else:
        print("\t\t FAIL: not allowed to remove element from the empty list")

    print("\t Trying to remove min element which is at the first position")
    # The expected behaviour is that the size of the list should be changed and the min_value is the first value
    list_test1 = create_list([-11, 3, -7, 2, 11, 5], list_class)
    print("\t\t List before remove: " + str(list_test1))
    s = list_test1.size()
    first_element = list_test1.first()
    min_value = list_test1.remove_min()
    # Check min value
    if min_value == first_element:
        print("\t\t PASS: first element is returned")
    else:
        print("\t\t FAIL: the return value is not equal to the first element - " + str(min_value))
    # Check List size
    if list_test1.size() == s - 1:
        print("\t\t PASS: list size is decreased")
    else:
        print("\t\t FAIL: list size is not decreased")
    print("\t\t List after remove: " + str(list_test1))

    print("\t Trying to remove min element which is at last position")
    # The expected behaviour is that the size of the list should be changed and the min_value is the last value
    list_test2 = create_list([-11, 3, -7, 2, 11, -50], list_class)
    print("\t\t List before remove: " + str(list_test2))
    s = list_test2.size()
    last_element = list_test2.last()
    result = list_test2.remove_min()
    # Check min value
    if result == last_element:
        print("\t\t PASS: last element is returned")
    else:
        print("\t\t FAIL: the return value is not equal to the last element - " + str(result))
    # Check List size
    if list_test2.size() == s - 1:
        print("\t\t PASS: list size is decreased")
    else:
        print("\t\t FAIL: list size is not decreased")
    print("\t\t List after remove: " + str(list_test2))

    print("\t Trying to remove min element which is at some middle position")
    list_test3 = create_list([-1, 3, -7, 2, 11, -5], list_class)
    print("\t\t List before remove: " + str(list_test3))
    min_value = -7
    s = list_test3.size()
    result = list_test3.remove_min()
    # Check min value
    if result == min_value:
        print("\t\t PASS: min value element is returned")
    else:
        print("\t\t FAIL: the return value is not the min value - " + str(result))
    # Check List size
    if list_test3.size() == s - 1:
        print("\t\t PASS: list size is decreased")
    else:
        print("\t\t FAIL: list size is not decreased")
    print("\t\t List after remove: " + str(list_test3))


def test_linked_list_add_at_recursive():
    """This function is for testing Ex5"""

    print("Running task 5 tests for add_at method in LinkedList")

    print("\t Trying to add element at position 0 in empty list")
    # The expected behaviour is that the size of the list is not changed and the min_value is None
    empty_list = create_list([], SingleLinkedList)
    s = empty_list.size()
    try:
        empty_list.add_at(5, 0)
        print("\t\t FAIL: ValueError should be thrown as the list is empty and index is out of boundaries")
        if empty_list.size() == s:
            print("\t\t PASS: list size is not changed")
        else:
            print("\t\t FAIL: no element should be added to empty list")
    except ValueError:
        print("\t\t PASS: ValueError is thrown if the index is not valid")

    print("\t Trying to add element to non empty list at position equal to the list size")
    list_test1 = create_list([-11, 3, -7, 2, 11, 5], SingleLinkedList)
    print("\t\t List before invalid addition: " + str(list_test1))
    s = list_test1.size()
    try:
        list_test1.add_at(5, s)
        print("\t\t FAIL: ValueError should be thrown as the index is out of boundaries")
        if list_test1.size() == s:
            print("\t\t PASS: list size is not changed")
        else:
            print("\t\t FAIL: no element should be added to the list at invalid index")
    except ValueError:
        print("\t\t PASS: ValueError is thrown if the index is not valid")
    print("\t\t List after invalid addition: " + str(list_test1))

    print("\t Trying to add element to list at position 0")
    list_test1 = create_list([-11, 3, -7, 2, 11, 5], SingleLinkedList)
    print("\t\t List before addition: " + str(list_test1))
    s = list_test1.size()
    try:
        print("\t\t Adding 5 at position 0")
        list_test1.add_at(5, 0)

        if list_test1.size() == s + 1:
            print("\t\t PASS: list size is increased")
        else:
            print("\t\t FAIL: list size is not increased")
        if 5 == list_test1.first():
            print("\t\t PASS: first element is added")
        else:
            print("\t\t FAIL: the new element is not added at first position")
        print("\t\t List after  addition: " + str(list_test1))
    except ValueError:
        print("\t\t FAIL: ValueError should not be thrown as the index is valid")

    print("\t Trying to add element to list at mid position")
    list_test1 = create_list([-11, 3, -7, 2, 11, 5], SingleLinkedList)
    print("\t\t List before addition: " + str(list_test1))
    s = list_test1.size()
    try:
        print("\t\t Adding 17 at position " + str(list_test1.size() // 2))
        list_test1.add_at(17, list_test1.size() // 2)

        if list_test1.size() == s + 1:
            print("\t\t PASS: list size is increased")
        else:
            print("\t\t FAIL: list size is not increased")
        print("\t\t List after  addition: " + str(list_test1))
    except ValueError:
        print("\t\t FAIL: ValueError should not be thrown as the index is valid")


def test_array_list_step_iterator():
    """This function is for testing Ex3"""

    print("Running task 3 tests for StepIterator of ArrayList")
    print("\t Trying to iterate over the ArrayList elements with step 0")
    al = create_list([1, 2, 3, 4], ArrayList)
    has_exception = False
    try:
        it = al.step_iterator(0)
    except TypeError:
        print(f"\t\t FAIL: The step_iterator method does not return an iterator object")
    except ValueError:
        has_exception = True
        print("\t\t PASS: ValueError is thrown during iterator creation")
    if not has_exception:
        print("\t\t FAIL: ValueError is not thrown during iterator creation")

    print("\t Trying to iterate over the ArrayList elements with step 2")
    al = create_list([1, 2, 3, 4, 5, 6], ArrayList)
    it = al.step_iterator(2)
    print("\t\t List : " + str(al))
    res = create_list([], ArrayList)
    while True:
        try:
            s = next(it)
            res.add_last(s)
        except TypeError:
            print(f"\t\t FAIL: The step_iterator method does not return an iterator object")
            break
        except StopIteration:
            if res.size() == 3:
                print(f"\t\t PASS: Step iterator passed over 3 elements: " + str(res))
            else:
                print(f"\t\t FAIL: Step iterator passed over {res.size()} elements instead of 3: " + str(res))
            break

    print("\t Trying to iterate over the ArrayList elements with step larger than the list size")
    al = create_list([1, 2, 3, 4, 5, 6], ArrayList)
    it = al.step_iterator(al.size() + 1)
    print("\t\t List : " + str(al))
    res = create_list([], DoubleLinkedList)
    while True:
        try:
            s = next(it)
            res.add_last(s)
        except TypeError:
            print(f"\t\t FAIL: The step_iterator method does not return an iterator object")
            break
        except StopIteration:
            if res.size() == 1:
                print(f"\t\t PASS: Step iterator passed over only first element: " + str(res))
            else:
                print(f"\t\t FAIL: Step iterator passed over {res.size()} elements instead of 1: " + str(res))
            break

    print("\t Trying to iterate over the ArrayList elements using foreach loop")
    al = create_list([1, 2, 3, 4, 5, 6], ArrayList)
    print("\t\t List : " + str(al))
    res = create_list([], DoubleLinkedList)
    try:
        print(f"\t\t See the iteration result below and confirm it is as expected")
        print(f"\t\t", end=" ")
        for e in al:
            print(str(e), end=" ")
            res.add_last(e)
        print()
    except TypeError:
        print(f"\t\t FAIL: ArrayList is not iterable")


def test_get_max_stack_recursive_method():
    """This function is for testing Ex4"""
    print("Running task 4 tests for get_max_element method in LinkedStack class.")

    print("\t Trying to get max element of the empty stack")
    # The expected behaviour is that None is returned
    empty_stack = create_stack([])
    result = get_max_element(empty_stack)
    if result == 0:
        print("\t\t PASS: 0 is returned as max element of empty stack")
    else:
        print("\t\t FAIL: for the empty stack max value should be 0")

    print("\t Trying to get max element which is the top element")
    # The expected behaviour is that the top element is returned
    stack_test1 = create_stack([-11, 3, -7, 2, 11, 55])
    print("\t\t Stack : " + str(stack_test1))
    content_before = str(stack_test1)
    top_element = stack_test1.top()
    result = get_max_element(stack_test1)
    content_after = str(stack_test1)
    # Check max value
    if result == top_element:
        print("\t\t PASS: top element is returned")
    else:
        print("\t\t FAIL: the return value is not equal to the top element - " + str(result))
    # Check content
    if content_before == content_after:
        print("\t\t PASS: stack content is not changed")
    else:
        print("\t\t FAIL: stack content is changed")

    print("\t Trying to get max element which is the bottom element")
    # The expected behaviour is that the bottom element is returned
    stack_test2 = create_stack([16, 3, -7, 2, 11, 5])
    print("\t\t Stack : " + str(stack_test2))
    content_before = str(stack_test2)
    bottop_element = 16
    result = get_max_element(stack_test2)
    content_after = str(stack_test2)
    # Check max value
    if result == bottop_element:
        print("\t\t PASS: bottom element is returned")
    else:
        print("\t\t FAIL: the return value is not equal to the bottom element - " + str(result))
    # Check content
    if content_before == content_after:
        print("\t\t PASS: stack content is not changed")
    else:
        print("\t\t FAIL: stack content is changed")

    print("\t Trying to get max element which is at some middle position")
    stack_test3 = create_stack([-1, 3, 75, 2, 11, -5])
    print("\t\t Stack : " + str(stack_test3))
    max_value = 75
    result = get_max_element(stack_test3)
    # Check min value
    if result == max_value:
        print("\t\t PASS: max value element is returned")
    else:
        print("\t\t FAIL: the return value is not the max value - " + str(result))
    # Check content
    if content_before == content_after:
        print("\t\t PASS: stack content is not changed")
    else:
        print("\t\t FAIL: stack content is changed")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Uncomment next line for testing Ex1
    test_list_remove_min(1, ArrayList)

    # Uncomment next line for testing Ex2
    test_list_remove_min(2, SingleLinkedList)

    # Uncomment next line for testing Ex3
    test_array_list_step_iterator()

    # Uncomment next line for testing Ex4
    test_get_max_stack_recursive_method()

    # Uncomment next line for testing Ex5
    test_linked_list_add_at_recursive()




