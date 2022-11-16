#!/usr/bin/python3

import sys
import threading

sys.setrecursionlimit(10**8) # max depth of recursion
threading.stack_size(2**30)  # new thread will get stack of such size


def non_decreasing(L):
    return all(x <= y for x, y in zip(L, L[1:]))


def in_order(tree, result=[], parent=0):
    if parent == -1:
        return
    in_order(tree, result, tree[parent][1])
    result.append(tree[parent][0])
    in_order(tree, result, tree[parent][2])
    return result


def IsBinarySearchTree(tree):
    if len(tree) <= 1:
        return True
    results = in_order(tree)
    return non_decreasing(results)


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    if IsBinarySearchTree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()
