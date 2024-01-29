from red_black_tree import RedBlackTree  # StepInOrderIterator
from avl_tree import AVLTree  # StepPostOrderIterator
from my_collections import my_set, Map
from stack import Stack
from university_management import Student, Gender


class TreeSet(my_set):
    def __init__(self):
        self.__tree = RedBlackTree()

    def add(self, value: object) -> bool:
        return self.__tree.add(value)

    def remove(self, value: object) -> bool:
        return self.__tree.remove(value)

    def contains(self, value: object) -> bool:
        return self.__tree.contains(value)

    def equals(self, s: "Set class") -> bool:
        return self.__tree.equals(s)

    def remove_element_at(self, index: int) -> object:
        return self.__tree.remove_element_at(index)

    def size(self) -> int:
        return self.__tree.size()

    def is_empty(self) -> bool:
        return self.__tree.is_empty()

    def empty(self) -> None:
        self.__tree.empty()

    def __str__(self) -> str:
        return self.__tree.__str__()

    def __iter__(self):
        return self.__tree.__iter__()

    def __next__(self):
        return self.__tree.__next__()

    def __len__(self) -> int:
        return self.__tree.__len__()

    def get_next_in_postorder(self, e: object) -> object:
        return self.__tree.next_in_posorder(e)

    def get_next_in_preorder(self, e: object) -> object:
        return self.__tree.next_in_preorder(e)

    def in_order_iterator(self, step):
        pass
        # my_iter = StepInOrderIterator(self.__tree, step)
        # return my_iter

    def print(self) -> None:
        self.__tree.print()


class TreeMap(Map):
    def __init__(self):
        self.__tree = AVLTree()

    def put(self, key: object, value: object) -> object:
        return self.__tree.add(key, value)

    def get(self, key: object) -> object:
        return self.__tree.get(key)

    def remove(self, key: object) -> object:
        return self.__tree.remove(key)

    def size(self) -> int:
        return self.__tree.size()

    def is_empty(self) -> bool:
        return self.__tree.is_empty()

    def empty(self) -> None:
        self.__tree.empty()

    def __str__(self) -> str:
        return self.__tree.__str__()

    def __iter__(self):
        return self.__tree.__iter__()

    def __next__(self):
        return self.__tree.__next__()

    def __len__(self) -> int:
        return self.__tree.__len__()

    def get_ceiling_entry(self, e: "Node") -> "Node":
        return self.__tree.get_ceiling_entry(e)

    def get_floor_entry(self, e: "Node") -> "Node":
        return self.__tree.get_floor_entry(e)

    def get_unique_values(self) -> list:
        return self.__tree.get_unique_values()

    def post_order_iterator(self, step):
        pass
        # my_iter = StepPostOrderIterator(self.__tree, step)
        # return my_iter


# print("Creating 10 students and adding to a TreeSet")
# students = TreeSet()
#
# student_1 = Student(9, ['Calculus'], 0, "Aram", "Mkheyan", 2002, Gender.MALE, "weirdo_weirdoyan_2023@gmail.com", False)
# student_2 = Student(2, ["CS12423"], 4, 'Nane', "whateveryan", 2002, Gender.MALE, "weirdo_weirdoyan_2023@gmail.com", False)
# student_3 = Student(2, ["CS^%$^&"], 21, 'Vasak', 'mkrtchyan', 2002, Gender.MALE, "weirdo_weirdoyan_2023@gmail.com", False)
# student_4 = Student(2, ["CS876567"],3,'Karen', 'manukyan', 2002, Gender.MALE, "weirdo_weirdoyan_2023@gmail.com", False)
# student_5 = Student(43, ["CS76545678"], 8, 'Khoren','mikaelian', 2002, Gender.MALE, "weirdo_weirdoyan_2023@gmail.com", False)
# student_6 = Student(2, ["CS567y8u"], 9, 'Whatever',  'abdulyan', 2002, Gender.MALE, "weirdo_weirdoyan_2023@gmail.com", False)
# student_7 = Student(3, ["CSi76543"], 8,'More_Whatever', 'dambulyan', 2002, Gender.MALE, "weirdo_weirdoyan_2023@gmail.com", False)
# student_8 = Student(5, ["CS654redfghj"], 5,'Even_More_Whateverer', 'daxosyan', 2002, Gender.MALE, "weirdo_weirdoyan_2023@gmail.com", False)
# student_9 = Student(2345, ["CS34567890"], 4,'No_WOrds_Could_describe_the_usefuleness', 'lazyan',  2002, Gender.MALE, "weirdo_weirdoyan_2023@gmail.com", False)
# student_10 = Student(345, ["CS34567890"], 4,'LASSSSSSTTTTTT_ONEEEEEEEEEEEEEEEEEEEEEEEEEEEE',  'finalyan', 2002, Gender.MALE, "weirdo_weirdoyan_2023@gmail.com", False)
#
# students.add(student_1)
# students.add(student_2)
# students.add(student_3)
# students.add(student_4)
# students.add(student_5)
# students.add(student_6)
# students.add(student_7)
# students.add(student_8)
# students.add(student_9)
# students.add(student_10)
#
# print("Iterating over the TreeSet using in-order iterator")
# my_iterator = students.in_order_iterator(1)
# for i in my_iterator:
#     print(i.name, i.surname)

tree = AVLTree()
tree.add(100)
tree.add(50)
tree.add(150)
tree.add(25)
tree.add(75)
tree.add(125)
tree.add(175)
tree.add(110)
tree.add(130)
print(tree)


class StepPreOrderIterator:
    def __init__(self, tree, step):
        if step <= 0:
            raise ValueError("Step must be greater than 0")
        self.tree = tree
        self.step = step
        self.stack = []
        self.stack.append(self.tree._root)

    def get_next(self):
        if len(self.stack) != 0:
            returnable = self.stack.pop()
            if returnable is None:
                raise StopIteration
            if returnable.right:
                self.stack.append(returnable.right)
            if returnable.left:
                self.stack.append(returnable.left)
            return returnable.data
        else:
            raise StopIteration

    def __next__(self):
        for i in range(self.step):
            value = self.get_next()
        return value

    def __iter__(self):
        return self


def get_min(node):
    if not node:
        return None
    while node.left:
        node = node.left
    return node


class StepPostOrderIterator:
    def __init__(self, root, step=1):
        self.step = step
        self.current = get_min(root)
        while self.current and self.current.right:
            self.current = get_min(self.current.right)

    def get_next(self):
        if not self.current:
            raise StopIteration
        result = self.current
        parent = self.current.parent
        if not parent:
            self.current = None
        elif not parent.right or parent.right == result:
            self.current = parent
        else:
            self.current = get_min(parent.right)
            while self.current and self.current.right:
                self.current = get_min(self.current.right)

        return result.data

    def __next__(self):
        for i in range(self.step):
            result = self.get_next()
        return result

    def __iter__(self):
        return self


def get_max(node):
    if not node:
        return None
    while node.right:
        node = node.right
    return node


class StepReversePostOrderIterator:
    def __init__(self, root, step=1):
        self.step = step
        self.current = get_max(root)
        while self.current and self.current.left:
            self.current = get_max(self.current.left)

    def get_next(self):
        if not self.current:
            raise StopIteration
        result = self.current
        parent = self.current.parent
        if not parent:
            self.current = None
        elif not parent.left or parent.left == result:
            self.current = parent
        else:
            self.current = get_max(parent.left)
            while self.current and self.current.left:
                self.current = get_max(self.current.left)

        return result.data

    def __next__(self):
        for i in range(self.step):
            result = self.get_next()
        return result

    def __iter__(self):
        return self


def post_order_traversal(root):
    if not root:
        return
    post_order_traversal(root.left)
    post_order_traversal(root.right)
    print(root.data)


def post_order_traversal_iterative(root):
    if not root:
        return
    stack = [root]
    while stack:
        node = stack.pop()
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
        print(node.data)


print("Getting next of element using post order traversal")
# print(get_next_post_order(tree._root, 25))
post_order_traversal_iterative(tree._root)

# IN ORDER STUFF

# def get_min_node(node):
#     if not node:
#         return None
#     while node.left:
#         node = node.left
#     return node
#
#
# class InOrderIterator:
#     def __init__(self, root, step=1):
#         self.root = root
#         self.step = step
#         if not root:
#             return
#
#         self.stack = [root]
#         while root.left:
#             root = root.left
#             self.stack.append(root)
#         # self.get_next()
#         # self.step = 2
#
#     def __next__(self):
#         for i in range(self.step):
#             result = self.get_next()
#         return result
#
#     def get_next(self):
#         if not self.stack:
#             raise StopIteration
#         node = self.stack.pop()
#         current = node.right
#         while current:
#             self.stack.append(current)
#             current = current.left
#         return node.data
#
#     def __iter__(self):
#         return self
#
#
# class ReverseInOrderIterator:
#     def __init__(self, root, step: int):
#         self.root = root
#         self.step = step
#         if not root:
#             return
#         self.stack = [root]
#         while root.right:
#             root = root.right
#             self.stack.append(root)
#
#     def __next__(self):
#         for i in range(self.step):
#             result = self.get_next()
#         return result
#
#     def get_next(self):
#         if not self.stack:
#             raise StopIteration
#         node = self.stack.pop()
#         current = node.left
#         while current:
#             self.stack.append(current)
#             current = current.right
#         return node.data
#
#     def __iter__(self):
#         return self
#
#
# print("Get next in order after given element")
#
# def in_order_traversal(root):
#     if not root:
#         return
#     in_order_traversal(root.left)
#     print(root.data)
#     in_order_traversal(root.right)
#
#
# def get_next_in_order(root, e):
#     """Getting next element after given element"""
#     if not root:
#         return None
#     stack = [root]
#     while root.left:
#         root = root.left
#         stack.append(root)
#
#     while stack:
#         node = stack.pop()
#         if node.data == e:
#             if node.right:
#                 return get_min_node(node.right).data
#             if not stack:
#                 return None
#             return stack.pop().data
#         if node.right:
#             node = node.right
#             stack.append(node)
#             while node.left:
#                 node = node.left
#                 stack.append(node)
#
#
# def get_max_node(node):
#     if not node:
#         return None
#     while node.right:
#         node = node.right
#     return node
#
#
# def get_previous_in_order(root, e):
#     """Getting previous element after given element"""
#     if not root:
#         return None
#     stack = [root]
#     while root.right:
#         root = root.right
#         stack.append(root)
#
#     while stack:
#         node = stack.pop()
#         if node.data == e:
#             if node.left:
#                 return get_max_node(node.left).data
#             if not stack:
#                 return None
#             return stack.pop().data
#         if node.left:
#             node = node.left
#             stack.append(node)
#             while node.right:
#                 node = node.right
#                 stack.append(node)

print("Level order functions")


class LevelOrderIterator:
    def __init__(self, root, step=1):
        self.root = root
        self.step = step
        if not root:
            return
        self.queue = [root]

    def __next__(self):
        for i in range(self.step):
            result = self.get_next()
        return result

    def get_next(self):
        if not self.queue:
            raise StopIteration
        node = self.queue.pop(0)
        if node.left:
            self.queue.append(node.left)
        if node.right:
            self.queue.append(node.right)
        return node.data

    def __iter__(self):
        return self


class ReverseLevelOrderIterator:
    def __init__(self, root, step=1):
        self.root = root
        self.step = step
        if not root:
            return
        self.queue = [root]

    def __next__(self):
        for i in range(self.step):
            result = self.get_next()
        return result

    def get_next(self):
        if not self.queue:
            raise StopIteration
        node = self.queue.pop(0)
        if node.right:
            self.queue.append(node.right)
        if node.left:
            self.queue.append(node.left)
        return node.data

    def __iter__(self):
        return self


def level_order_traversal(root):
    if not root:
        return
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
        print(node.data)


print("Running level order traversal")
level_order_traversal(tree._root)
print("Running level order traversal using iterator")
level_order_iterator = LevelOrderIterator(tree._root, 2)
for i in level_order_iterator:
    print(i)
