# The aim is to design a queue abstract data type with the help of stacks.
class Queue:
    def __init__(self):
        # use one stack for enqueue operation
        self.enqueue_stack = []
        # use another stack for dequeue operation
        self.dequeue_stack = []

    # adding an item to the queue is O(1) operation
    def enqueue(self, data):
        self.enqueue_stack.append(data)

    # getting item
    def dequeue(self):
        # maybe there is no element left to dequeue
        if len(self.enqueue_stack) == 0 and len(self.dequeue_stack) == 0:
            raise Exception("Stacks are empty ... ")
        # if the dequeue stack is empty we have to items O(n) time
        if len(self.dequeue_stack) == 0:
            while len(self.enqueue_stack):
                self.dequeue_stack.append(self.enqueue_stack.pop())
        # otherwise, we just have to pop off an item in O(1)
        return self.dequeue_stack.pop()


# if __name__ == '__main__':
#     queue = Queue()
#     queue.enqueue(10)
#     queue.enqueue(18)
#     queue.enqueue(30)
#     print(queue.dequeue())
#     queue.enqueue(100)
#     print(queue.dequeue())
#     print(queue.dequeue())
#     print(queue.dequeue())
#     print(queue.dequeue())
