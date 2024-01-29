from double_queue import Node, DoubleLinkedListDeque
from circular_array import CircularArray

def test_double_linked_list():
    print("Running the tester for double linked list queue using assert")
    double_linked_list = DoubleLinkedListDeque()
    print("Checking if the queue is empty")
    try:
        assert double_linked_list.size() == 0
    except AssertionError:
        print("AssertionError")
        print("Expected: ", 0)
        print("Actual: ", double_linked_list.size())
    for i in range(1, 11):
        double_linked_list.enqueue(i)
    print("Checking enqueue")
    try:
        assert double_linked_list.size() == 10
    except AssertionError:
        print("AssertionError")
        print("Expected: ", 10)
        print("Actual: ", double_linked_list.size())
    print("Checking if the dequeue is working")
    try:
        assert double_linked_list.dequeue() == 1
    except AssertionError:
        print("AssertionError")
        print("Expected: ", 1)
        print("Actual: ", double_linked_list.dequeue())
    print("Checking the right dequeue")
    try:
        assert double_linked_list.right_dequeue() == 10
    except AssertionError:
        print("AssertionError")
        print("Expected: ", 10)
        print("Actual: ", double_linked_list.right_dequeue())
    print("Checking the left enqueue")
    double_linked_list.left_enqueue(1)
    try:
        assert double_linked_list.dequeue() == 1
    except AssertionError:
        print("AssertionError")
        print("Expected: ", 1)
        print("Actual: ", double_linked_list.dequeue())


def test_circular_array():
    print("Test cases for circular array using assertions")
    circular_array = CircularArray()
    for i in range(10):
        circular_array.enqueue(i)
    print(circular_array)
    print("Testing size, front, back, dequeue, swap")

    try:
        assert circular_array.size() == 10
    except AssertionError:
        print("AssertionError")
        print("Expected: ", 10)
        print("Actual: ", circular_array.size())
    else:
        print("size passed")

    try:
        assert circular_array.front() == 0
    except AssertionError:
        print("AssertionError")
        print("Expected: ", 0)
        print("Actual: ", circular_array.front())
    else:
        print("front passed")
    try:
        assert circular_array.back() == 9
    except AssertionError:
        print("AssertionError")
        print("Expected: ", 9)
        print("Actual: ", circular_array.back())
    else:
        print("back passed")
    try:
        assert circular_array.dequeue() == 0
    except AssertionError:
        print("AssertionError")
        print("Expected: ", 0)
        print("Actual: ", circular_array.dequeue())
    else:
        print("dequeue passed")
    try:
        print(circular_array)
        circular_array.swap(6, 1)
        print(circular_array)
    except AssertionError:
        print("AssertionError")
        print("Expected: ", "1 -> 0 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8")
        print("Actual: ", circular_array)


if __name__ == '__main__':
    # Test 1
    test_double_linked_list()

    # Test 2
    test_circular_array()
