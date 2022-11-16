import sys
from collections import deque


def distance(edge, s, t):
    dist = [float("inf")] * len(edge)
    dist[s] = 0
    q = deque()
    q.append(s)
    while len(q) > 0:
        u = q.popleft()
        for v in edge[u]:
            if dist[v] == float("inf"):
                q.append(v)
                dist[v] = dist[u] + 1
    if dist[t] == float("inf"):
        return -1
    else:
        return dist[t]


if __name__ == '__main__':
    inputs = sys.stdin.read()
    data = list(map(int, inputs.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
