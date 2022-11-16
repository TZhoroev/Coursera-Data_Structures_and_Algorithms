# python3

import sys
import threading


def compute_height(n, parents):
    parent_family = {i: [] for i in range(n)}
    for i, item in enumerate(parents):
        if item != -1:
            parent_family[item].append(i)
        else:
            head = i
    stages = parent_family[head]
    count = 1

    while len(stages) > 0:
        parents = []
        count += 1
        for item in stages:
            parents.extend(parent_family[item])
        stages = parents
    return count


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**29)   # new thread will get stack of such size
threading.Thread(target=main).start()
