from my_collections import Collection
from stack import myStack as LinkedListStack


# class StepInOrderIterator:
#     def update_stack(self, tree, stack):
#         while tree.left:
#             stack.append(tree)
#             tree = tree.left
#         stack.append(tree)
#         return stack
#
#     def __init__(self, tree, step):
#         if step <= 0:
#             raise ValueError("Step must be greater than 0")
#         self.tree = tree
#         self.step = step
#         self.stack = []
#         if self.tree._root:
#             self.stack = self.update_stack(self.tree._root, self.stack)
#
#     def get_next(self):
#         if len(self.stack) != 0:
#             returnable = self.stack.pop()
#             if returnable is None:
#                 raise StopIteration
#             if returnable.right:
#                 self.stack = self.update_stack(returnable.right, self.stack)
#
#             return returnable.data
#         else:
#             raise StopIteration
#
#     def __next__(self):
#         for i in range(self.step):
#             value = self.get_next()
#         return value
#
#     def __iter__(self):
#         return self

# class StepPostOrderIterator:
#     def __init__(self, tree, step):
#         if step <= 0:
#             raise ValueError("Step must be greater than 0")
#         self.tree = tree
#         self.step = step
#         self.stack = []
#         self.stack.append(self.tree._root)
#
#     def get_next(self):
#         if len(self.stack) != 0:
#             returnable = self.stack.pop()
#             if returnable is None:
#                 raise StopIteration
#             if returnable.right:
#                 self.stack.append(returnable.right)
#             if returnable.left:
#                 self.stack.append(returnable.left)
#             return returnable.data
#         else:
#             raise StopIteration
#
#     def __next__(self):
#         for i in range(self.step):
#             value = self.get_next()
#         return value
#
#     def __iter__(self):
#         return self


# class StepPreOrderIterator:
#     def __init__(self, tree, step):
#         if step <= 0:
#             raise ValueError("Step must be greater than 0")
#         self.tree = tree
#         self.step = step
#         self.stack = []
#         self.stack.append(self.tree._root)
#
#     def get_next(self):
#         if len(self.stack) != 0:
#             returnable = self.stack.pop()
#             if returnable is None:
#                 raise StopIteration
#             if returnable.right:
#                 self.stack.append(returnable.right)
#             if returnable.left:
#                 self.stack.append(returnable.left)
#             return returnable.data
#         else:
#             raise StopIteration
#
#     def __next__(self):
#         for i in range(self.step):
#             value = self.get_next()
#         return value
#
#     def __iter__(self):
#         return self


class AVLTree(Collection):
    class _Node:
        def __init__(self, data, parent=None, left=None, right=None):
            self.data = data
            self.parent = parent
            self.left = left
            self.right = right
            self.height = 1

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

    def add(self, el: object) -> bool:
        self.insert_rec(el)
        return True

    def remove(self, el: object) -> bool:
        self.remove_rec(el)
        return True

    def has(self, el: object) -> bool:
        pass

    @staticmethod
    def node_height(node):
        if not node:
            return 0
        return node.height

    @staticmethod
    def get_balance(node):
        if not node:
            return 0
        return AVLTree.node_height(node.left) - AVLTree.node_height(node.right)

    @staticmethod
    def right_rotate(y):
        if not y:
            return

        x = y.left
        T2 = x.right

        # rotate
        x.right = y

        x.parent = y.parent
        y.parent = x

        y.left = T2
        if T2:
            T2.parent = y

        # update heights
        y.height = 1 + max(AVLTree.node_height(y.left), AVLTree.node_height(y.right))
        x.height = 1 + max(AVLTree.node_height(x.left), AVLTree.node_height(x.right))
        return x

    @staticmethod
    def left_rotate(node):
        if not node:
            return
        y = node.right
        T2 = y.left
        # rotate
        y.left = node
        y.parent = node.parent
        node.parent = y
        node.right = T2
        if T2:
            T2.parent = node
        # update heights
        node.height = 1 + max(
            AVLTree.node_height(node.left), AVLTree.node_height(node.right)
        )
        y.height = 1 + max(AVLTree.node_height(y.left), AVLTree.node_height(y.right))
        return y

    def insert_rec(self, el: object):
        self._root = self.insert_rec_helper(self._root, None, el)
        self._size += 1

    @staticmethod
    def insert_rec_helper(node, parent, el):
        # if node:
        #     print("Inserting " + str(el) + " into " + str(node.data))
        # else:
        #     print("Inserting " + str(el) + " into " + str(node))

        if not node:
            return AVLTree._Node(el, parent=parent)
        if el > node.data:
            # print(f"{el} is greater than {node.data}")
            node.right = AVLTree.insert_rec_helper(node.right, node, el)
        else:
            # print(f"{el} is less than {node.data}")
            node.left = AVLTree.insert_rec_helper(node.left, node, el)
        # update height
        node.height = 1 + max(
            AVLTree.node_height(node.left), AVLTree.node_height(node.right)
        )
        # print(f"Node {node.data} has height {node.height}")
        # if node.parent:
        #     print(f"Node {node.data} has parent {node.parent.data}")
        # else:
        #     print(f"Node {node.data} has no parent")

        # # get balance
        balance = AVLTree.get_balance(node)
        # print(f"Balance factor for {node.data} is {balance}")

        # # check balance factor and rebalance tree
        if balance > 1:
            # Left-Left or Left-Right Case
            if el <= node.left.data:
                # print("Left-Left case for the " + str(node.data))
                # Left-Left Case
                # print("Right rotating " + str(node.data))
                return AVLTree.right_rotate(node)
            else:
                # print("Left-Right case for the " + str(node.data))
                # Left-Right Case
                # Left Rotate node.left
                # print("Left rotating " + str(node.left.data))
                node.left = AVLTree.left_rotate(node.left)
                return AVLTree.right_rotate(node)
        elif balance < -1:
            # Right-Left or Right-Right Case
            if el <= node.right.data:
                # print("Right-Left case for the " + str(node.data))
                # Right-Left Case
                node.right = AVLTree.right_rotate(node.right)
                # print("Left rotating " + str(node.data))
                return AVLTree.left_rotate(node)
            else:
                # print("Right-Right case for the " + str(node.data))
                # Right-Right Case
                # print("Left rotating " + str(node.data))
                return AVLTree.left_rotate(node)
        return node

    def remove_rec(self, el: object) -> bool:
        if not self.contains(el):
            return False
        self._root = self.remove_rec_helper(self._root, el)
        self._size -= 1
        return True

    def remove_rec_helper(self, node, el):
        if not node:
            return node
        if el < node.data:
            node.left = self.remove_rec_helper(node.left, el)
        elif el > node.data:
            node.right = self.remove_rec_helper(node.right, el)
        else:
            # node with one child or no child
            if not node.left:
                temp = node.right
                node = None
                return temp
            elif not node.right:
                temp = node.left
                node = None
                return temp
            # node with two children
            temp = self.get_min_left(node.right)
            node.data = temp.data
            node.right = self.remove_rec_helper(node.right, temp.data)
        # update height
        node.height = 1 + max(
            AVLTree.node_height(node.left), AVLTree.node_height(node.right)
        )
        # get balance
        balance = AVLTree.get_balance(node)
        # check balance factor and rebalance tree
        if balance > 1:
            # Left-Left or Left-Right Case
            if AVLTree.get_balance(node.left) >= 0:
                # Left-Left Case
                return AVLTree.right_rotate(node)
            else:
                # Left-Right Case
                node.left = AVLTree.left_rotate(node.left)
                return AVLTree.right_rotate(node)
        elif balance < -1:
            # Right-Left or Right-Right Case
            if AVLTree.get_balance(node.right) <= 0:
                # Right-Right Case
                return AVLTree.left_rotate(node)
            else:
                # Right-Left Case
                node.right = AVLTree.right_rotate(node.right)
                return AVLTree.left_rotate(node)
        return node

    def element(self, node):
        if not node:
            return None
        return node.data

    def __str__(self):
        if not self._root:
            return ""
        ret_string = ""
        current_level = [self._root]
        while current_level:
            next_level = []
            for node in current_level:
                ret_string += str(node.data) + ",h=" + str(node.height) + ",  "
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current_level = next_level
            ret_string += "\n"
        return ret_string

    def print(self) -> None:
        print(self)
        # self.LevelOrder(self._root)

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
        current = AVLTree.get_min_left(self, self._root)
        while current:
            # visit node
            tree_nodes.append(current)
            # get next node
            if current.right:
                current = AVLTree.get_min_left(self, current.right)
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
            while root.left:
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
            self.PreOrder_rec(node.left)
        if node.right:
            self.PreOrder_rec(node.right)

    def PreOrder_iterative(self):
        stack = []
        stack.append(self._root)
        while len(stack) > 0:
            node = stack.pop()
            print(node.data)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    # POST ORDER TRAVERSAL
    def PostOrder_rec(self, node):
        if node.left:
            self.PostOrder_rec(node.left)
        if node.right:
            self.PostOrder_rec(node.right)
        print(node.data)

    def PostOrder_iterative(self):
        stack = []
        stack.append(self._root)
        my_list = []
        while len(stack) > 0:
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

    def level_order_recursive(self):
        self.level_order_rec(self.root)

    @staticmethod
    def level_order_rec(node):
        pass

    # def LevelOrder(self, node):
    #     queue = []
    #     queue.append(node)
    #     while(len(queue) > 0):
    #         print(queue[0].data)
    #         node = queue.pop(0)
    #         if node.left:
    #             queue.append(node.left)
    #         if node.right:
    #             queue.append(node.right)

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

    def find_max(self, node=None):
        if node is None:
            node = self._root
        if node.right:
            return self.find_max(node.right)
        return node

    def find_min(self, node=None):
        if node is None:
            node = self._root
        if node.left:
            return self.find_min(node.left)
        return node

    def get_ceiling_entry(self, el: _Node) -> _Node:
        if not self._root or not el:
            return None
        stack = []
        my_list = []
        stack.append(self._root)
        while len(stack) > 0:
            node = stack.pop()
            my_list.append(node.data)
            if node.data == el:
                break
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        if node.parent:
            return node.parent.data
        else:
            return None

    def get_floor_entry(self, el: _Node) -> _Node:
        if not self._root or not el:
            return None
        stack = []
        my_list = []
        stack.append(self._root)
        while len(stack) > 0:
            node = stack.pop()
            my_list.append(node.data)
            if node.data == el:
                break
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        my_list.reverse()
        if node.left:
            return node.left.data
        elif node.right:
            return node.right.data
        else:
            return None

    def get_unique_values(self) -> list:
        if not self._root:
            return []
        stack = []
        my_list = []
        stack.append(self._root)
        while len(stack) > 0:
            node = stack.pop()
            if node.data not in my_list:
                my_list.append(node.data)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return my_list

    def is_tree_complete(self, node=None, index=0):
        if node is None:
            node = self._root
        if node is None:
            return True
        current_level = [self._root]
        index = 0
        while current_level:
            next_level = []
            for node in current_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current_level = next_level
            if not next_level:
                break
            index += 1
            if 2**index != len(current_level):
                return False
        return True

    def is_tree_left_skewed(self) -> bool:
        node = self._root
        if node == None or (node.left == None and node.right == None):
            return True
        if node.left and node.right:
            return False
        if node.left:
            return self.is_tree_left_skewed(node.left)
        return self.is_tree_left_skewed(node.right)

    @staticmethod
    def get_minimum(node):
        if node.left:
            return AVLTree.get_minimum(node.left)
        return node

    def get_next_postorder(self, e):
        if not self._root:
            return None
        stack = []
        my_list = []
        stack.append(self._root)
        while len(stack) > 0:
            node = stack.pop()
            my_list.append(node.data)
            if node.data == e:
                break
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        my_list.reverse()
        print(my_list)
        return my_list[my_list.index(e) - 1]

    def get_previous_postorder(self, e):
        if not self._root:
            return None
        stack = []
        my_list = []
        stack.append(self._root)
        while len(stack) > 0:
            node = stack.pop()
            my_list.append(node.data)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        my_list.reverse()
        print(my_list)
        return my_list[my_list.index(e) - 1]


# LEVEL ORDERS

# class LevelOrderIterator:
#     def __init__(self, root):
#         if not root:
#             return
#         self.queue = [root]
#
#     def __next__(self):
#         if not self.queue:
#             raise StopIteration
#         node = self.queue.pop(0)
#         if node.left:
#             self.queue.append(node.left)
#         if node.right:
#             self.queue.append(node.right)
#         return node.data
#
#     def __iter__(self):
#         return self


# class OddLevelIterator:
#     def __init__(self, root):
#         if not root:
#             return
#         # ODD level iterator
#
#         self.queue = []
#         if root.left:
#             self.queue.append(root.left)
#         if root.right:
#             self.queue.append(root.right)
#
#         # Even Level Iterator
#
#         # self.queue = [root]
#
#     def __next__(self):
#         if not self.queue:
#             raise StopIteration
#         node = self.queue.pop(0)
#         if node.left:
#             if node.left.left:
#                 self.queue.append(node.left.left)
#             if node.left.right:
#                 self.queue.append(node.left.right)
#         if node.right:
#             if node.right.left:
#                 self.queue.append(node.right.left)
#             if node.right.right:
#                 self.queue.append(node.right.right)
#         return node.data
#
#     def __iter__(self):
#         return self


# class StepLevelIterator:
#     def __init__(self, root, step):
#         if not root:
#             return
#         if step <= 0:
#             raise ValueError("Step must be greater than 0")
#         self.step = step
#         self.queue = [root]
#         self.root = root
#         # self.first = True
#
#     def __next__(self):
#         # if self.first:
#         #     self.first = False
#         #     return [self.root]
#         for i in range(self.step):
#             level = self.__get_next()
#         return level
#
#     def __get_next(self):
#         next_level = []
#         if not self.queue:
#             raise StopIteration
#         while self.queue:
#             node = self.queue.pop(0)
#             if node.left:
#                 next_level.append(node.left)
#             if node.right:
#                 next_level.append(node.right)
#         self.queue = next_level
#         return next_level
#
#     def __iter__(self):
#         return self
#
#
# class ReverseLevelIterator:
#     def __init__(self, root):
#         if not root:
#             return
#         self.queue = [root]
#         self.lavel_matrix = [[root]]
#
#         while self.queue:
#             next_level = []
#             while self.queue:
#                 node = self.queue.pop(0)
#                 if node.left:
#                     next_level.append(node.left)
#                 if node.right:
#                     next_level.append(node.right)
#             self.lavel_matrix.append(list(next_level))
#             self.queue = next_level
#
#     def __next__(self):
#         if not self.lavel_matrix:
#             raise StopIteration
#         return self.lavel_matrix.pop(-1)
#
#     def __iter__(self):
#         return self


# IN ORDER ITERATORS


class StepInOrderIterator:
    def update_stack(self, tree, stack):
        while tree.left:
            stack.append(tree)
            tree = tree.left
        stack.append(tree)
        return stack

    def __init__(self, root, step):
        if step <= 0:
            raise ValueError("Step must be greater than 0")
        self.root = root
        self.step = step
        self.stack = []

        if self.root:
            self.stack = self.update_stack(self.root, self.stack)

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

    def __iter__(self):
        return self


class ReverseInOrderIterator:
    def update_stack(self, node, step):
        while node.right:
            self.stack.append(node)
            self.step = step
            node = node.right

    def __init__(self, root):
        if not root:
            return

        self.stack = []
        self.root = root
        self.update_stack(self.root)

    def __next__(self):
        returnable = self.stack.pop()
        if not returnable.parent:
            return returnable

        if not returnable.parent.left:
            return


#
# print("Creating an AVL Tree")
# tree = AVLTree()
# tree.add(30)
# tree.add(21)
# tree.add(44)
# tree.add(12)
# tree.add(25)
# tree.add(41)
# tree.add(47)
# print(tree)
#
# my_iterator = StepInOrderIterator(tree._root, 3)
# for i in my_iterator:
#     print(i)

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
