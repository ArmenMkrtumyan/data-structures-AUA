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


class RedBlackTree(Collection):
    class _Node:
        def __init__(self, data, parent=None, left=None, right=None, color="RED"):
            self.data = data
            self.parent = parent
            self.left = left
            self.right = right
            self.color = color

        def get_sibling(self):
            if not self.parent:
                return None
            if self == self.parent.left:
                return self.parent.right
            else:
                return self.parent.left

        def near_nephew(self):
            sibling = self.get_sibling()
            if not sibling:
                return None

            if self == self.parent.left:
                return sibling.left
            else:
                return sibling.right

        def far_nephew(self):
            sibling = self.get_sibling()
            if not sibling:
                return None
            if self == self.parent.left:
                return sibling.right
            else:
                return sibling.left

        @staticmethod
        def is_double_black(node):
            if not node:
                return False
            return node.color == "DOUBLE_BLACK"

        def get_uncle(self):
            if not self.parent and not self.parent.parent:
                return None
            elif self.parent == self.parent.parent.left:
                return self.parent.parent.right
            else:
                return self.parent.parent.left

        def recolor(self):
            if self.color == "RED":
                self.color = "BLACK"
            else:
                self.color = "RED"

        def color_black(self):
            self.color = "BLACK"

        def color_red(self):
            self.color = "RED"

        def color_double_black(self):
            self.color = "DOUBLE_BLACK"

        @staticmethod
        def is_red(node):
            if not node:
                return False
            return node.color == "RED"

        @staticmethod
        def is_black(node):
            if not node:
                return True
            return node.color == "BLACK"

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
        self.insert_iterative(el)
        return True

    def remove(self, el: object) -> bool:
        self.delete(el)
        return True

    def get_max(node):
        if node.right:
            return RedBlackTree.get_max(node.right)
        return node

    def delete(self, el):
        if not self._root:
            return

        # Step 1: Find the node
        current = self._root
        while current and current.data != el:
            if el < current.data:
                current = current.left
            elif el > current.data:
                current = current.right

        if not current:
            # el is not in RBT
            return

        if current.left and current.right:
            new_node = RedBlackTree.get_max(current.left)
            current.data = new_node.data
            current = new_node

        rep_node = current.left if current.left else current.right
        # here current is leaf or has 1 child
        if RedBlackTree._Node.is_black(current):
            # if deleted node is black
            # if rep_node is red, then just color it black and exit
            if RedBlackTree._Node.is_red(rep_node):
                rep_node.color_black()
            else:
                current.color_double_black()
            self.fix_delete(current)

        # update parent
        if rep_node:
            rep_node.parent = current.parent
        # update child relationship
        if not current.parent:
            self._root = rep_node
        elif current == current.parent.left:
            current.parent.left = rep_node
        else:
            current.parent.right = rep_node
        self._size -= 1

    def fix_delete(self, node):
        if not node:
            return

        if not self._Node.is_double_black(node):
            return

        parent = node.parent
        # Case 1: if node is root node
        if not parent:
            node.color_black()
            return

        s = node.get_sibling()
        nn = node.near_nephew()
        fn = node.far_nephew()

        # Case 2.1: if s is black, nn and fn are black, parent is red
        if (
            self._Node.is_black(s)
            and self._Node.is_black(nn)
            and self._Node.is_black(fn)
            and self._Node.is_red(parent)
        ):
            s.color_red()
            node.color_black()
            parent.color_black()

        # Case 2.2: if s is black, nn and fn are black, parent is black
        elif (
            self._Node.is_black(s)
            and self._Node.is_black(nn)
            and self._Node.is_black(fn)
            and self._Node.is_black(parent)
        ):
            s.color_red()
            node.color_black()
            parent.color_double_black()
            # new double black node is parent
            self.fix_delete(parent)

        # Case 3: sibling is red
        elif self._Node.is_red(s):
            parent.color, s.color = s.color, parent.color
            # rotate parent in node's direction
            if node == parent.left:
                self.left_rotate(parent)
            else:
                self.right_rotate(parent)
            self.fix_delete(node)

        # Case 4: sibling is black, fn is black and nn is red
        elif (
            self._Node.is_black(s) and self._Node.is_black(fn) and self._Node.is_red(nn)
        ):
            nn.color, s.color = s.color, nn.color
            if nn == s.left:
                self.right_rotate(s)
            else:
                self.left_rotate(s)
            self.fix_delete(node)

        # Case 5: sibling is black and fn is red
        elif self._Node.is_black(s) and self._Node.is_red(fn):
            parent.color, s.color = s.color, parent.color
            if node == parent.left:
                self.left_rotate(parent)
            else:
                self.right_rotate(parent)
            fn.color_black()
            node.color_black()

    def has(self, el: object) -> bool:
        pass

    def right_rotate(self, y):
        if not y:
            return

        x = y.left
        T2 = x.right

        # rotate
        x.right = y
        parent = y.parent
        if not parent:
            self._root = y
        elif y == parent.left:
            parent.left = x
        else:
            parent.right = x

        x.parent = y.parent
        y.parent = x

        y.left = T2
        if T2:
            T2.parent = y

        return x

    def left_rotate(self, x):
        if not x:
            return

        y = x.right
        T2 = y.left

        # rotate
        y.left = x
        parent = x.parent
        if not parent:
            self._root = y
        elif x == parent.left:
            parent.left = y
        else:
            parent.right = y

        y.parent = x.parent
        x.parent = y

        x.right = T2
        if T2:
            T2.parent = x

        return y

    def reconstruct(self, node):
        if not node:
            return

        parent = node.parent
        if not parent:
            node.color_black()
            return

        if self._Node.is_black(parent):
            return

        grandparent = parent.parent
        if not grandparent:
            parent.color_black()
            return

        uncle = node.get_uncle()
        if self._Node.is_red(uncle):
            # Case 1: uncle is red, parent is red
            parent.color_black()
            uncle.color_black()
            grandparent.color_red()
            self.reconstruct(grandparent)

        elif parent == grandparent.left and node == parent.left:
            # Case 2: uncle is black, LEFT LEFT CASE
            self.right_rotate(grandparent)
            grandparent.color, parent.color = parent.color, grandparent.color
        elif parent == grandparent.left and node == parent.right:
            # Case 3: uncle is black, LEFT RIGHT CASE
            self.left_rotate(parent)
            self.right_rotate(grandparent)
            grandparent.color, node.color = node.color, grandparent.color
        elif parent == grandparent.right and node == parent.right:
            # Case 4: uncle is black, RIGHT RIGHT CASE
            self.left_rotate(grandparent)
            grandparent.color, parent.color = parent.color, grandparent.color
        elif parent == grandparent.right and node == parent.left:
            # Case 5: uncle is black, RIGHT LEFT CASE
            self.right_rotate(parent)
            self.left_rotate(grandparent)
            grandparent.color, node.color = node.color, grandparent.color

    def insert_iterative(self, el: object):
        # Step 1: Insert el as in BST
        current, parent = self._root, None
        while current:
            parent = current
            if el < current.data:
                current = current.left
            else:
                current = current.right

        new_node = RedBlackTree._Node(el, parent)
        if not parent:
            self._root = new_node
        elif el > parent.data:
            parent.right = new_node
        else:
            parent.left = new_node
        self._size += 1

        # Step 2: Reconstruct and recolor
        self.reconstruct(new_node)

    def insert_rec(self, el: object):
        self._root = self.insert_rec_helper(self._root, None, el)
        self._size += 1

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
                ret_string += str(node.data) + ", color: " + str(node.color) + ",    "
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current_level = next_level
            ret_string += "\n"
        return ret_string

    def print(self) -> None:
        print(self)

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
        current = RedBlackTree.get_min_left(self, self._root)
        while current:
            # visit node
            tree_nodes.append(current)
            # get next node
            if current.right:
                current = RedBlackTree.get_min_left(self, current.right)
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

    def previous_in_preorder(self, el):
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
        if node.parent.left != node and node.parent.left:
            return node.parent.left.data
        elif node.parent.right != node and node.parent.right:
            return node.parent.right.data
        elif node.parent:
            return node.parent.data
        else:
            return None

    def next_in_preorder(self, el):
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
    def LevelOrder(self, node):
        queue = []
        queue.append(node)
        while len(queue) > 0:
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


# print("Creating a Red Black Tree")
# tree = RedBlackTree()
# print("Adding 10 elements")
# tree.add(10)
# tree.add(20)
# tree.add(30)
# tree.add(45)
# tree.add(55)
# tree.add(60)
# print("Printing the tree")
# tree.print()

# print("Printing the tree using iterator")
# for i in tree:
#     print(i)
# print("Printing the tree using iterator with step 2")
# my_iter = tree.InorderIterator(2)
# for i in my_iter:
#     print(i)

# print("Removing 40")
# tree.remove(40)
# tree.print()
#
# print("Removing 60")
# tree.remove(60)
# tree.print()
#
# print("Removing 50")
# tree.remove(50)
# tree.print()
#
# print("Removing 20")
# tree.remove(20)
# tree.print()

#
# print("Removing 30")
# tree.remove_rec(30)
# tree.print()

# print(tree)
# print(f"Tring out different traversal methods")
# print("InOrder")
# tree.PrintInOrder(tree._root)
# print("PreOrder")
# tree.PreOrder_rec(tree._root)
# print("PostOrder")
# tree.PostOrder_rec(tree._root)
# print("LevelOrder")
# tree.LevelOrder(tree._root)

# print("Testing the next and previous in preorder")
# tree.PreOrder_rec(tree._root)
# print("_____________________________")
# print(f"Next of 40 was {tree.next_in_preorder(45)}")
# print(f"Previous for 60 was {tree.previous_in_preorder(45)}")
