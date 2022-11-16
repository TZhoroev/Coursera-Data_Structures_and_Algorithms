import sys
from collections import deque


def distance(edge, s):
    dist = [float("inf")] * len(edge)  # prev = [None] * len(edge)
    dist[s] = 0
    q = deque()
    q.append(s)
    while len(q) > 0:
        u = q.popleft()
        for v in edge[u]:
            if dist[v] == float("inf"):
                q.append(v)
                dist[v] = dist[u] + 1  # prev[v] = u
            else:
                if (dist[u] - dist[v]) % 2 == 0:
                    return False
    return True


# construct the path from s to u.
def reconstruct_path(s, u, prev):
    result = []
    while u != s:
        result.append(u)
        u = prev[u]
    result.reverse()
    return result


def bipartite(edge):
    if distance(edge, 1):
        return 1
    return 0


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
    print(bipartite(adj))
