# python3
from collections import deque


class StackWithMax:

    def __init__(self):
        self.__stack = deque()
        self.max_stack = []

    def push(self, a):
        self.__stack.append(a)
        if len(self.max_stack) == 0:
            self.max_stack.append(a)
        elif a >= self.max_stack[-1]:
            self.max_stack.append(a)

    def pop(self):
        assert(len(self.__stack))
        b = self.__stack.popleft()
        if b == self.max_stack[-1]:
            self.max_stack.pop()

    def max(self):
        return self.max_stack[-1]

    def ext(self, data):
        self.__stack.extend(data)
        self.max_stack.append(max(data))


def max_sliding_window_naive(sequence, m):
    maximums = deque()
    n_size= len(sequence)
    for i in range(m):
        while maximums and sequence[i] >= sequence[maximums[-1]]:
            maximums.pop()
        maximums.append(i)
    for i in range(m, n_size):
        print(str(sequence[maximums[0]]) + " ", end="")
        while maximums and maximums[0] <= i-m:
            maximums.popleft()
        while maximums and sequence[i] >= sequence[maximums[-1]] :
            maximums.pop()
        maximums.append(i)
    print(str(sequence[maximums[0]]))


if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    max_sliding_window_naive(input_sequence, window_size)

