# python3
import sys
import threading
sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 26)  # new thread will get stack of such size


class Vertex:
    def __init__(self, weight):
        self.weight = weight
        self.children = []


def ReadTree():
    size = int(input())
    tree = [Vertex(w) for w in map(int, input().split())]
    for i in range(1, size):
        a, b = list(map(int, input().split()))
        tree[a - 1].children.append(b - 1)
        tree[b - 1].children.append(a - 1)
    return tree


def dfs(tree, vertex, parent, D):
    if D[vertex] == -1:
        if len(tree[vertex].children) == 1 and vertex != 0: D[vertex] = tree[vertex].weight
        else:
            m1 = tree[vertex].weight
            for u in tree[vertex].children:
                if u != parent: m1 += sum([dfs(tree, w, u, D) for w in tree[u].children if w != vertex])
            m0 = sum([dfs(tree, u, vertex, D) for u in tree[vertex].children if u != parent])
            D[vertex] = max(m1, m0)
    return D[vertex]


def MaxWeightIndependentTreeSubset(tree):
    size = len(tree)
    if size == 0: return 0
    D = [-1] * size
    d = dfs(tree, 0, -1, D)
    return d


def main():
    tree = ReadTree()
    weight = MaxWeightIndependentTreeSubset(tree)
    print(weight)


if __name__ == '__main__':
    # This is to avoid stack overflow issues
    threading.Thread(target=main).start()
