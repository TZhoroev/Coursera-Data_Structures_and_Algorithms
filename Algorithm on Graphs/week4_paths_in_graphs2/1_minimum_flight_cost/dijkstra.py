import sys
from collections import defaultdict
from heapq import heappop, heappush


def distance(edge, weights, s_vertex, t_vertex):
    dist = defaultdict(lambda: float('inf'))
    prev = defaultdict(lambda: None)
    dist[s_vertex] = 0
    h = []
    heappush(h, (0, s_vertex))
    while h:
        _, u = heappop(h)
        if u == t_vertex:
            return dist[t_vertex]
        for v, weight_uv in zip(edge[u], weights[u]):
            if dist[v] > dist[u] + weight_uv:
                dist[v] = dist[u] + weight_uv
                prev[v] = u
                heappush(h, (dist[v], v))
    return -1


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
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
