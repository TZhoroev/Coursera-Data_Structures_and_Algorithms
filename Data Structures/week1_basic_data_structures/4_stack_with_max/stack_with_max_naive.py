# python3
from collections import deque
import sys


class StackWithMax:

    def __init__(self):
        self.__stack = []
        self.max_stack = []

    def push(self, a):
        self.__stack.append(a)
        if len(self.max_stack) == 0:
            self.max_stack.append(a)
        elif a >= self.max_stack[-1]:
            self.max_stack.append(a)

    def pop(self):
        assert(len(self.__stack))
        b = self.__stack.pop()
        if b == self.max_stack[-1]:
            self.max_stack.pop()

    def max(self):
        return self.max_stack[-1]


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.push(int(query[1]))
        elif query[0] == "pop":
            stack.pop()
        elif query[0] == "max":
            print(stack.max())
        else:
            assert 0
