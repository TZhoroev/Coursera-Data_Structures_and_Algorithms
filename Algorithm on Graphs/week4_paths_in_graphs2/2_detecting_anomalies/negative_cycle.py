import sys
from collections import defaultdict


def negative_cycle(edge, weights, n_len):

    dist = [10**9] * n_len
    prev = [None] * n_len
    dist[0] = 0
    cycle = []
    for i in range(len(edge)):
        for u in range(len(edge)):
            for v, weight_uv in zip(edge[u], weights[u]):
                if dist[v] > dist[u] + weight_uv:
                    dist[v] = dist[u] + weight_uv
                    prev[v] = u
                    if i == (len(edge) - 1):
                        cycle.append(v)
    if cycle:
        return 1
    return 0


if __name__ == '__main__':
    inputs = sys.stdin.read()
    data = list(map(int, inputs.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost, n))
