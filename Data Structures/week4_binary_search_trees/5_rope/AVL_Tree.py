class Node:
    def __init__(self, data, parent):
        self.data = data
        self.parent = parent
        self.left_child = None
        self.right_child = None
        self.height = 0



class AVLTree:
    def __init__(self):
        # we can access to the root node exclusively.
        self.root = None

    def insert(self, data):
        self.root = Node(data, None) if self.root is None else self.insert_node(data, self.root)

    def insert_node(self, data, node):
        # we have to go left subtree, check if the left subtree exists.
        if data < node.data:
            if node.left_child: self.insert_node(data, node.left_child)
            else:
                node.left_child = Node(data, node)
                # update the heights
                node.height = max(self.calc_height(node.left_child), self.calc_height(node.right_child)) + 1
        # if not case then we have to traverse right subtree, then check if the left subtree exists.
        else:
            if node.right_child: self.insert_node(data, node.right_child)
            else:
                node.right_child = Node(data, node)
                node.height = max(self.calc_height(node.left_child), self.calc_height(node.right_child)) + 1
        # after every insertion we have to check whether the AVL properties are violated
        self.handle_violation(node)

    def remove(self, data):
        if self.root is not None:
            self.remove_node(data, self.root)

    def remove_node(self, data, node):
        if node is None: return
        if data < node.data: self.remove_node(data, node.left_child)
        elif data > node.data: self.remove_node(data, node.right_child)
        else: # after finding the node we remove it from the AVL tree
            # case 1) if the node is leaf node
            if node.left_child is None and node.right_child is None:
                parent = node.parent
                if parent is not None and parent.left_child == node: parent.left_child = None
                if parent is not None and parent.right_child == node: parent.right_child = None
                if parent is None: self.root = None
                self.handle_violation(parent)
                del node
            # case 2) if the node has single child (right)
            elif node.left_child is None and node.right_child is not None:
                parent = node.parent
                if parent is not None and parent.left_child == node: parent.left_child = node.left_child
                elif parent is not None and parent.right_child == node: parent.right_child = node.right_child
                else: self.root = node.right_child
                node.right_child.parent = parent
                self.handle_violation(parent)
                del node
            # case 3) if the node has single child (left)
            elif node.left_child is not None and node.right_child is None:
                parent = node.parent
                if parent is not None and parent.left_child == node: parent.left_child = node.left_child
                elif parent is not None and parent.right_child == node: parent.right_child = node.right_child
                else: self.root = node.left_child
                node.left_child.parent = parent
                self.handle_violation(parent)
                del node
            # the node has 2 children
            else:
                predecessor = self.get_predecessor(node.left_child)
                temporary_node = predecessor.data
                predecessor.data = node.data
                node.data = temporary_node
                self.remove_node(data, predecessor)

    def get_predecessor(self, node):
        if node.right_child: return self.get_predecessor(node.right_child)
        return node
    
    def calc_height(self, node):
        if node is None:
            return -1
        return node.height

    def calculate_balance(self, node):
        if node is None: return 0
        return self.calc_height(node.left_child) - self.calc_height(node.right_child)

    def handle_violation(self, node):
        # check the nodes from the node we have inserted up to the root
        while node:
            node.height = max(self.calc_height(node.right_child), self.calc_height(node.left_child)) + 1
            self.violation_helper(node)
            # whenever we settle violation (rotations) it may happen that it
            # violates the AVL properties in other part of the tree.
            node = node.parent

    def violation_helper(self, node):
        balance = self.calculate_balance(node)
        # we know the tree is left heavy, but it can be left-left heavy or left-right heavy
        if balance > 1:
            # left heavy situation: left rotation on parent + right rotation on grandparent
            if self.calculate_balance(node.left_child) < 0:  # check right rotation
                self.rotate_left(node.left_child)
            # this ie right rotation on grandparent (if left-left then only we have right rotation, otherwise left-right)
            self.rotate_right(node)
        # we know that tree is right heavy, but it can be right-left or right-right.
        if balance < -1:
            # right heavy situation: right rotation on parent + left rotation on grandparent
            if self.calculate_balance(node.right_child) > 0:  # check left rotation
                self.rotate_right(node.right_child)
            # this ie left rotation on grandparent (if right-right then only we have left rotation, otherwise right-left)
            self.rotate_left(node)

    def rotate_right(self, node):
        temp_left_child, t = node.left_child, node.left_child.right_child
        temp_left_child.right_child, node.left_child = node, t
        if t is not None:
            t.parent = node
        temp_parent, node.parent = node.parent, temp_left_child
        temp_left_child.parent = temp_parent

        if temp_left_child.parent is not None and temp_left_child.parent.left_child == node:
            temp_left_child.parent.left_child = temp_left_child
        if temp_left_child.parent is not None and temp_left_child.parent.right_child == node:
            temp_left_child.parent.right_child = temp_left_child
        if node == self.root:
            self.root = temp_left_child
        node.height = max(self.calc_height(node.left_child), self.calc_height(node.right_child)) + 1
        temp_left_child.height = max(self.calc_height(temp_left_child.left_child),
                                     self.calc_height(temp_left_child.right_child)) + 1

    def rotate_left(self, node):
        temp_right_child, t = node.right_child, node.right_child.left_child
        temp_right_child.left_child, node.right_child = node, t
        if t is not None:
            t.parent = node
        temp_parent, node.parent = node.parent, temp_right_child
        temp_right_child.parent = temp_parent

        if temp_right_child.parent is not None and temp_right_child.parent.left_child == node:
            temp_right_child.parent.left_child = temp_right_child
        if temp_right_child.parent is not None and temp_right_child.parent.right_child == node:
            temp_right_child.parent.right_child = temp_right_child
        if node == self.root:
            self.root = temp_right_child
        node.height = max(self.calc_height(node.left_child), self.calc_height(node.right_child)) + 1
        temp_right_child.height = max(self.calc_height(temp_right_child.left_child),
                                      self.calc_height(temp_right_child.right_child)) + 1

    def traverse(self):
        if self.root is not None:
            self.traverse_in_order(self.root)

    def traverse_in_order(self, node):
        if node.left_child:
            self.traverse_in_order(node.left_child)
        l, r, p = " ", " ", " "
        if node.left_child is not None: l = node.left_child.data
        else: l = "NULL"
        if node.right_child is not None: r = node.right_child.data
        else: r = "NULL"
        if node.parent is not None: p = node.parent.data
        else: p = "NULL"
        print("%s left: %s right: %s")
