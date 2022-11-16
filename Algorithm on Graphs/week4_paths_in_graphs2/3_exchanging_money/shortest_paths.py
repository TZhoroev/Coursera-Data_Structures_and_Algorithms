import sys
from collections import deque


def shortest_path(edge, weights, s, distance, n_len):
    prev = [None] * n_len
    distance[s] = 0
    cycle = deque()
    for i in range(n_len):
        for u in range(n_len):
            for v, weight_uv in zip(edge[u], weights[u]):
                if distance[u] != float("inf") and distance[v] > distance[u] + weight_uv:
                    distance[v] = distance[u] + weight_uv
                    prev[v] = u
                    if i == (len(edge) - 1):
                        cycle.append(v)
    visited = [False]*n_len
    while cycle:
        u = cycle.popleft()
        visited[u] = True
        distance[u] = "-"
        for v in edge[u]:
            if not visited[v]:
                cycle.append(v)
    return distance


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
    source = data[0]
    source -= 1
    distances = [float("inf")] * n
    distances = shortest_path(adj, cost, source, distances, n)
    for d in distances:
        if d == float("inf"):
            print("*")
        else:
            print(d)
