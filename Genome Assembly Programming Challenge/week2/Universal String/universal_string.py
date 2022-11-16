# python3
import sys
from collections import defaultdict


def pre_process(k):
    last = '1' * k
    bin_integer, penultimate = int(last, 2), "1" + ('0' * (k - 1))
    beginning = '0' * k
    adj = defaultdict(lambda: [])
    for index in range(0, bin_integer + 1):
        current = (bin(index)[2:].zfill(k))
        if current != penultimate and current != beginning:
            string = current[:(k - 1)]
            edge = current[1:k]
            adj[string].append(edge)
            adj[edge].append(string)
    return adj


def euler_path(k, adj):
    start = '0' * (k - 1)
    tour = [start]
    current = start
    while len(adj[current]) > 0:
        suffix = current[1:]
        next_Char = "1" if suffix + "1" in adj[current] else "0"
        tour.append(suffix + next_Char)
        adj[current].remove(suffix + next_Char)
        adj[suffix + next_Char].remove(current)
        current = suffix + next_Char
    return tour


def print_k_mer(path):
    res = '0'
    for i, d in enumerate(path): res += d[0]
    print(res)


if __name__ == "__main__":
    n = int(sys.stdin.read().strip())
    edges = pre_process(n)
    paths = euler_path(n, edges)
    print_k_mer(paths)
