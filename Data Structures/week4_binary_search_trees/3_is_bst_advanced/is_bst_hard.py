#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**8) # max depth of recursion
threading.stack_size(2**30)  # new thread will get stack of such size


def non_bst(L, tree):
    for x, y in zip(L, L[1:]):
        if tree[x][0] > tree[y][0]:
            return False
        if tree[x][0] == tree[y][0] and tree[x][2] == -1:
            return False
    return True


def in_order(tree, result=[], parent=0):
    if parent == -1:
        return
    in_order(tree, result, tree[parent][1])
    result.append(parent)
    in_order(tree, result, tree[parent][2])
    return result


def IsBinarySearchTree(tree):
    if len(tree) <= 1:
        return True
    results = in_order(tree)
    return non_bst(results, tree)


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
