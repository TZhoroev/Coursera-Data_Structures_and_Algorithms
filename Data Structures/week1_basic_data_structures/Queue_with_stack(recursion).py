# The aim is to design a queue abstract data type with the help of stacks.
class Queue:
    def __init__(self):
        self.stack = []

    def enqueue(self, data):
        self.stack.append(data)

    # Note: we use two stacks again but instead of explicitly define the second stack we use
    # the call stack of program recursively
    def dequeue(self):
        if len(self.stack) == 0:
            raise Exception("No element in stack")
        # base case for the recursive calls is the firsts item
        if len(self.stack) == 1:
            return self.stack.pop()
        # we keep popping items until we found the last one
        item = self.stack.pop()
        dequeued_item = self.dequeue()
        # after finding the item we insert items one by one
        self.stack.append(item)
        return dequeued_item


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(18)
    queue.enqueue(30)
    print(queue.dequeue())
    queue.enqueue(100)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())

