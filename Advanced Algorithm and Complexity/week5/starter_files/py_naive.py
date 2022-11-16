# python3
import sys
from collections import defaultdict


def Solution():
    D = defaultdict(lambda: 0)
    n = int(sys.stdin.readline().strip())
    t = int(sys.stdin.readline().strip())
    for _ in range(n):
        id, value = [int(i) for i in sys.stdin.readline().strip().split()]
        D[id] = value

    for _ in range(n):
        id, value = [int(i) for i in sys.stdin.readline().strip().split()]
        D[id] -= value
    _ = int(sys.stdin.readline().strip())
    queries = list(map(int, sys.stdin.readline().strip().split()))
    for query in queries:
        if D[query] >= t: print("1 ", end="")
        else: print("0 ", end="")


if __name__ == '__main__':
    Solution()
