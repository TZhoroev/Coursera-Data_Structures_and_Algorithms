# python3

import sys
import threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeOrders:
    def __init__(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for _ in range(self.n)]
        self.left = [0 for _ in range(self.n)]
        self.right = [0 for _ in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def in_order(self, result=[], parent=0):  # sorted order
        if parent == -1:
            return
        self.in_order(result, self.left[parent])
        result.append(self.key[parent])
        self.in_order(result, self.right[parent])
        return result

    def pre_order(self, result=[], parent=0):
        if parent == -1:
            return
        result.append(self.key[parent])
        self.pre_order(result, self.left[parent])
        self.pre_order(result, self.right[parent])
        return result

    def post_order(self, result=[], parent=0):
        if parent == -1:
            return
        self.post_order(result, self.left[parent])
        self.post_order(result, self.right[parent])
        result.append(self.key[parent])
        return result


def main():
    tree = TreeOrders()
    print(" ".join(str(x) for x in tree.in_order()))
    print(" ".join(str(x) for x in tree.pre_order()))
    print(" ".join(str(x) for x in tree.post_order()))


threading.Thread(target=main).start()
