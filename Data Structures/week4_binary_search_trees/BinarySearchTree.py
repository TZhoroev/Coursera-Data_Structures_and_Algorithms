class Node:
    def __init__(self, data, parent):
        self.data = data
        self.parent = parent
        self.left_child = None
        self.right_child = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = Node(data, None) if not self.root else self.insert_node(data, self.root)

    def insert_node(self, data, node):
        # we have to go left subtree, check if the left subtree exists.
        if data < node.data:
            if node.left_child: self.insert_node(data, node.left_child)
            else: node.left_child = Node(data, node)
        # if not case then we have to traverse right subtree, then check if the left subtree exists.
        else:
            if node.right_child: self.insert_node(data, node.right_child)
            else: node.right_child = Node(data, node)

    def remove(self, data):
        if self.root: self.remove_node(data, self.root)

    def remove_node(self, data, node):
        if node is None: return
        if data < node.data: self.remove_node(data, node.left_child)
        elif data > node.data: self.remove_node(data, node.right_child)
        else:
            # removing a leaf node
            if node.left_child is None and node.right_child is None:
                parent = node.parent
                if parent is not None and parent.left_child == node: parent.left_child = None
                if parent is not None and parent.right_child == node: parent.right_child = None
                if parent is None: self.root = None
                del node
            # remove node with right subtree exist
            elif node.left_child is None and node.right_child is not None:
                parent = node.parent
                if parent is not None and parent.left_child == node: parent.left_child = node.left_child
                elif parent is not None and parent.right_child == node: parent.right_child = node.right_child
                else: self.root = node.right_child
                node.right_child.parent = parent
                del node
            # remove node with left subtree exist
            elif node.right_child is None and node.left_child is not None:
                parent = node.parent
                if parent is not None and parent.left_child == node: parent.left_child = node.left_child
                elif parent is not None and parent.right_child == node: parent.right_child = node.right_child
                else: self.root = node.left_child
                node.left_child.parent = parent
                del node
            # removing the node with two children
            else:
                predecessor = self.get_predecessor(node.left_child)
                temporary_node = predecessor.data
                predecessor.data = node.data
                node.data = temporary_node
                self.remove_node(data, predecessor)

    def get_predecessor(self, node):
        if node.right_child: return self.get_predecessor(node.right_child)
        return node

    def traverse_in_order(self):
        if self.root: return self.traverse_in_orders(self.root, results=[])

    def traverse_in_orders(self, node, results):
        if node.left_child: self.traverse_in_orders(node.left_child, results)
        results.append(node.data)
        if node.right_child: self.traverse_in_orders(node.right_child, results)
        return results

    def traverse_pre_order(self):
        if self.root: return self.traverse_pre_orders(self.root, results=[])

    def traverse_pre_orders(self, node, results):
        results.append(node.data)
        if node.left_child: self.traverse_pre_orders(node.left_child, results)
        if node.right_child: self.traverse_pre_orders(node.right_child, results)
        return results

    def traverse_post_order(self):
        if self.root: return self.traverse_post_orders(self.root, results=[])

    def traverse_post_orders(self, node, results):
        if node.left_child: self.traverse_post_orders(node.left_child, results)
        if node.right_child: self.traverse_post_orders(node.right_child, results)
        results.append(node.data)
        return results

    def get_max_value(self):
        if self.root: return self.max_value(self.root)

    def max_value(self, node):
        if node.right_child: return self.max_value(node.right_child)
        return node.data

    def get_min_value(self):
        if self.root: return self.min_value(self.root)

    def min_value(self, node):
        if node.left_child: return self.min_value(node.left_child)
        return node.data


class TreeComparison:
    def compare_trees(self, tree1, tree2):
        # we have to check the base cases (it may be the child of a leaf node, so we have to use "==")
        if not tree1 and not tree2: return tree1 == tree2
        # if the values within the node is not the same we return False (topology of the trees are not same)
        if tree1.data is not tree2.data: return False
        # left subtree values and right subtree values must match as well!!
        return self.compare_trees(tree1.left_child, tree2.left_child) and self.compare_trees(tree1.right_child, tree2.right_child)


if __name__ == '__main__':

    # bts = BST()
    # bts.insert(3)
    # bts.insert(55)
    # bts.insert(-13)
    # bts.insert(76)
    # bts.insert(88)
    # bts.insert(-93)
    # print("In order traverse:", bts.traverse_in_order())
    # print("Pre order traverse: ", bts.traverse_pre_order())
    # print("Post order traverse:", bts.traverse_post_order())
    # print("Maximum element:", bts.get_max_value())
    # print("Minimum element:", bts.get_min_value())
    # bts.remove(88)
    # print("Maximum element:", bts.get_max_value())
    # print("In order traverse:", bts.traverse_in_order())
    # bts.remove(8908)
    # print("Maximum element:", bts.get_max_value())
    # print("In order traverse:", bts.traverse_in_order())

    bst1 = BST()
    bst1.insert(32)
    bst1.insert(45)
    bst1.insert(462)
    bst1.insert(87)
    bst1.insert(98)

    bst2 = BST()
    bst2.insert(32)
    bst2.insert(45)
    bst2.insert(462)
    bst2.insert(87)
    bst2.insert(98)
    comparator = TreeComparison()
    print(comparator.compare_trees(bst1.root, bst2.root))
