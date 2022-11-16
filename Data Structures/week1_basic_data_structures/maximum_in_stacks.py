class MaxStack:
    def __init__(self):
        # use one stack for enqueue operation
        self.main_stack = []
        # use another stack for dequeue operation
        self.max_stack = []

    # adding an item to the queue is O(1) operation
    def push(self, data):

        # push the new item onto the stack
        self.main_stack.append(data)
        # first item is same for both stacks
        if len(self.main_stack) == 1:
            self.max_stack.append(data)
            return
        # if the data is the largest element of the max_stack we insert it to the data
        if data > self.max_stack[-1]:
            self.max_stack.append(data)
        # otherwise, we duplicate the last element of the max_stack
        else:
            self.max_stack.append(self.max_stack[-1])

    # def getting items
    def pop(self):
        self.max_stack.pop()
        return self.main_stack.pop()

    # just returns the maximum element
    def get_max(self):
        return self.max_stack[-1]


if __name__ == '__main__':
    max_stack = MaxStack()
    max_stack.push(3)
    max_stack.push(5)
    max_stack.push(35)
    max_stack.push(54)
    max_stack.push(43)
    max_stack.push(67)
    max_stack.push(80)
    print(max_stack.get_max())
    print(max_stack.pop())
    print(max_stack.get_max())
