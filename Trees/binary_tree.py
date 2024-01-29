from my_collections import Collection
from stack import myStack as LinkedListStack

class StepInOrderIterator:
    def update_stack(self, tree, stack):
        while tree.left:
            stack.append(tree)
            tree = tree.left
        stack.append(tree)
        return stack

    def __init__(self, tree, step):
        self.tree = tree
        self.step = step
        self.stack = []
        if self.tree._root:
            self.stack = self.update_stack(self.tree._root, self.stack)

    def get_next(self):
        if len(self.stack) != 0:
            returnable = self.stack.pop()
            if returnable is None:
                raise StopIteration
            if returnable.right:
                self.stack = self.update_stack(returnable.right, self.stack)

            return returnable.data
        else:
            raise StopIteration

    def __next__(self):
        for i in range(self.step):
            value = self.get_next()
        return value

class BinarySearchTree(Collection):
    class _Node:
        def __init__(self, data, parent=None, left=None, right=None):
            self.data = data
            self.parent = parent
            self.left = left
            self.right = right

    def __init__(self):
        self._root = None
        self._size = 0

    def __iter__(self):
        return self.InorderIterator(1)

    def size(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    def empty(self):
        self._root = None
        self._size = 0

    def add (self, el: object) -> bool:
        self.insert_iterative(el)
        return True

    def remove(self, el: object) -> bool:
        removed = self.remove_iterative(el)
        if removed:
            self._size -= 1
        return removed

    def has(self, el: object) -> bool:
        pass

    def element(self, node):
        if not node:
            return None
        return node.data

    def print(self) -> None:
        self.LevelOrder(self._root)

    def get_min_left(self, node):
        if node.left:
            return self.get_min_left(node.left)
        return node

    def get_min(self, node, stack):
        if node.left:
            stack.push(node)
            return self.get_min(node.left, stack)
        stack.push(node)
        return node

    def PrintInOrder(self, node):
        if node.left:
            self.PrintInOrder(node.left)
        print(node.data)
        if node.right:
            self.PrintInOrder(node.right)
        return None

    def inorder_nodes_iterative(self) -> list:
        if not self._root:
            return []
        tree_nodes = []
        current = BinarySearchTree.get_min_left(self, self._root)
        while current:
            # visit node
            tree_nodes.append(current)
            # get next node
            if current.right:
                current = BinarySearchTree.get_min_left(self, current.right)
            else:
                parent = current.parent
                while parent and parent.right == current:
                    current, parent = parent, parent.parent
                current = parent
        return tree_nodes

    def inorder_nodes_with_stack(self):
        if not self._root:
            return []
        my_list = []
        my_stack = LinkedListStack()
        current = self.get_min(self._root, my_stack)
        print(f"Curent is {current.data}")

        while not my_stack.is_empty():
            element = my_stack.pop()
            my_list.append(element.data)
            if element.right:
                element = self.get_min(element.right, my_stack)
        return my_list

    def InorderIterator(self, step):
        return StepInOrderIterator(self, step)

    class InorderIterator_ITERATIVE:
        def __init__(self, root, step=1):
            while (root.left):
                root = root.left
            self.current = root
            self.step = step

        def get_next(self):
            if not self.current:
                raise StopIteration

            # read data
            current_data = self.current.data
            # prepare for the next iteration
            if self.current.right:
                current = self.current.right
                while current.left:
                    current = current.left
                self.current = current
            else:
                parent = self.current.parent
                while parent and parent.right == self.current:
                    self.current, parent = parent, parent.parent
                self.current = parent
            return current_data

        def __next__(self):
            for i in range(self.step):
                value = self.get_next()
            return value

    # PRE ORDER TRAVERSAL
    def PreOrder_rec(self, node):
        print(node.data)
        if node.left:
            self.PreOrder(node.left)
        if node.right:
            self.PreOrder(node.right)

    def PreOrder_iterative(self):
        stack = []
        stack.append(self._root)
        while(len(stack) > 0):
            node = stack.pop()
            print(node.data)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)


    # POST ORDER TRAVERSAL
    def PostOrder_rec(self, node):
        if node.left:
            self.PostOrder(node.left)
        if node.right:
            self.PostOrder(node.right)
        print(node.data)

    def PostOrder_iterative(self):
        stack = []
        stack.append(self._root)
        my_list = []
        while(len(stack) > 0):
            node = stack.pop()
            my_list.append(node.data)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        my_list.reverse()
        for i in my_list:
            print(i)



    # LEVEL ORDER TRAVERSAL
    def LevelOrder(self, node):
        queue = []
        queue.append(node)
        while(len(queue) > 0):
            print(queue[0].data)
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def root(self):
        return self._root

    def parent(self, node):
        if not node:
            return None
        return node.parent

    def children(self, node) -> list:
        if not node:
            return []
        children = []
        if node.left:
            children.append(node.left)
        if node.right:
            children.append(node.right)
        return children

    def is_root(self, node):
        if not node:
            return False
        return not node.parent

    def is_internal(self, node):
        if not node:
            return False
        has_parent = node.parent is not None
        is_leaf = not node.left and not node.right
        return has_parent and not is_leaf

    def is_external(self, node):  # or leaf
        return not self.is_root(node) and not self.is_internal(node)

    def insert_rec(self, el: object):
        self._root = self.insert_rec_helper(self._root, None, el)
        self._size += 1

    @staticmethod
    def insert_rec_helper(node, parent, el):
        if not node:
            return BinarySearchTree._Node(el, parent=parent)
        if el > node.data:
            node.right = BinarySearchTree.insert_rec_helper(node.right, node, el)
        else:
            node.left = BinarySearchTree.insert_rec_helper(node.left, node, el)
        return node

    def insert_iterative(self, el: object):
        if not self._root:
            self._root = BinarySearchTree._Node(el)
            self._size += 1
            return
        current = self._root
        while current:
            if el > current.data:
                if not current.right:
                    current.right = BinarySearchTree._Node(el, parent=current)
                    self._size += 1
                    return
                current = current.right
            else:
                if not current.left:
                    current.left = BinarySearchTree._Node(el, parent=current)
                    self._size += 1
                    return
                current = current.left

    def contains(self, el):
        if self.contains_helper(el, self._root):
            return True
        return False

    def contains_helper(self, el, root):
        if el == root.data:
            return True
        if root.left:
            if self.contains_helper(el, root.left):
                return True
        if root.right:
            if self.contains_helper(el, root.right):
                return True

    def remove_iterative(self, el: object) -> bool:
        if not self.contains(el):
            return False
        current = self._root
        while current:
            if el > current.data:
                current = current.right
            elif el < current.data:
                current = current.left
            else:
                if not current.left and not current.right:
                    if current == current.parent.right:
                        current.parent.right = None
                    else:
                        current.parent.left = None
                elif not current.left:
                    current.right.parent = current.parent
                    current = self.children(current)[1]
                    #current = current.right
                elif not current.right:
                    current.left.parent = current.parent
                    current = self.children(current)[0]
                    #current = current.left
                else:
                    min = self.get_min_left(current.right)
                    parent = min.parent
                    min.parent = None
                    current.data = min.data
                    if min.right:
                        min.right.parent = parent
                    if min == parent.left:
                        parent.left = min.right
                    else:
                        parent.right = min.right
                return True

    def remove_rec(self, el: object, node = None) -> bool:
        if node is None:
            node = self._root
        if not self.contains(el):
            return False
        if el > node.data:
            self.right = self.remove_rec(el, node.right)
        elif el < node.data:
            self.left = self.remove_rec(el, node.left)
        else:
            if not node.left and not node.right:
                if node == node.parent.right:
                    node.parent.right = None
                else:
                    node.parent.left = None
            elif not node.left:
                node.right.parent = node.parent
                node = self.children(node)[1]
            elif not node.right:
                node.left.parent = node.parent
                current = self.children(node)[0]
            else:
                min = self.get_min_left(node.right)
                node.data = min.data
                self.remove_rec(min.data, node.right)
            return True

    def find_max(self, node = None):
        if node is None:
            node = self._root
        if node.right:
            return self.find_max(node.right)
        return node

    def find_min(self, node = None):
        if node is None:
            node = self._root
        if node.left:
            return self.find_min(node.left)
        return node



print("Creating a Tree")
tree = BinarySearchTree()
tree.add(5)
tree.add(3)
tree.add(7)
tree.add(2)
tree.add(4)
tree.add(6)
tree.add(8)
print("Printing the Tree")
tree.print()

# print(tree.contains(2))
# a = 8
# print(f"Removing {a}")
# tree.remove(a)
# tree.print()
#
# print(f"Max is {tree.find_max().data}")
#
# if tree.contains(4):
#     print("APRES, XELACI EZ ES")
# else:
#     print("AY APUSH LAKOT")
#
# if tree.contains(100):
#     print("APRES, XELACI EZ ES")
# else:
#     print("AY APUSH LAKOT")
#
# print("IN ORDER ITERATIVE TRAVERSAL")
# in_order_list = tree.inorder_nodes_iterative()
# for node in in_order_list:
#     print(node.data)
# print(f"Returned{root.remove(12)}")
# print("""AFTER REMOVING 12""")
# root.LevelOrder()
# print(f"Returned{root.remove(90)}")
# print("""AFTER REMOVING 90""")
# root.LevelOrder()
# print(f"Returned{root.remove(24)}")
# print("""AFTER REMOVING 24""")
# root.LevelOrder()

# print("IN ORDER USING STACK")
# in_order_list = tree.inorder_nodes_with_stack()
# for node in in_order_list:
#     print(node)
#
# print("USING ITERATOR WITH STEP 1")
# in_order_iterator = tree.InorderIterator(1)
# try:
#     while True:
#         print(next(in_order_iterator))
# except StopIteration:
#     pass
#
# print("USING ITERATOR WITH STEP 2")
# in_order_iterator = tree.InorderIterator(2)
# try:
#     while True:
#         print(next(in_order_iterator))
# except StopIteration:
#     pass
#
# print("USING ITERATOR WITH STEP 3")
# in_order_iterator = tree.InorderIterator(3)
# try:
#     while True:
#         print(next(in_order_iterator))
# except StopIteration:
#     pass
#
# print("USING ITERATIVE ITERATOR with step 1")
# in_order_iterator = BinarySearchTree.InorderIterator_ITERATIVE(tree._root, 1)
# try:
#     while True:
#         print(next(in_order_iterator))
# except StopIteration:
#     pass
#
# print("USING ITERATIVE ITERATOR with step 2")
# in_order_iterator = BinarySearchTree.InorderIterator_ITERATIVE(tree._root, 2)
# try:
#     while True:
#         print(next(in_order_iterator))
# except StopIteration:
#     pass
#
# print("USING ITERATIVE ITERATOR with step 3")
# in_order_iterator = BinarySearchTree.InorderIterator_ITERATIVE(tree._root, 3)
# try:
#     while True:
#         print(next(in_order_iterator))
# except StopIteration:
#     pass
#
# print("USING ITERATIVE ITERATOR with step 10")
# in_order_iterator = BinarySearchTree.InorderIterator_ITERATIVE(tree._root, 10)
# try:
#     while True:
#         print(next(in_order_iterator))
# except StopIteration:
#     pass
#
# print("Using a for loop and stack step iterator")
# for i in tree:
#     print(i)

print("POST ORDER TRAVERSAL ITERATIVE")
tree.PostOrder_iterative()
