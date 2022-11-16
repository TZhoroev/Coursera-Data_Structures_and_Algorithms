class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class DoublyLinkedlist:

    def __init__(self):
        self.head = None
        self.tail = None
        self.numOfNodes = 0

    # this is insert node with O(1) complex time
    def insert_start(self, data):

        self.numOfNodes += 1
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.nextNode = self.head
            self.head = new_node

    # this is O(n) running time
    def insert_end(self, data):
        self.numOfNodes += 1
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        actual_node = self.head
        while actual_node.nextNode is not None:
            actual_node = actual_node.nextNode
        actual_node.nextNode = new_node

    def size_of_linkedlist(self):
        return self.numOfNodes

    # O(n)
    def traverse(self):
        actual_node = self.head
        while actual_node.nextNode is not None:
            print(actual_node.data)
            actual_node = actual_node.nextNode

    def remove(self, data):
        # this checks if there is any node in linked list
        if self.head is None:
            return

        actual_node = self.head
        previous_node = None
        while actual_node is not None and actual_node != data:
            previous_node = actual_node
            actual_node = actual_node.nextNode
    # if we come to the end of search it means that we have not found given data in the linked list
        if actual_node is None:
            return
    # if program runs until here it means we found the given data
        self.numOfNodes -= 1
        if previous_node is not None:
            # if the data is head of the linked list
            self.head = actual_node.nextNode
        else:
            # if the data anywhere except the head.
            # link previous to the next one omitting the desired data
            previous_node.nextNode = actual_node.nextNode
