
import sys


def explore(v, adjacent):
    visited[v] = True
    for w in adjacent[v]:
        if not visited[w]:
            explore(w, adjacent)
    return visited


def number_of_components(adjacent):
    global visited, cc
    for i in range(len(adjacent)):
        if not visited[i]:
            explore(i, adjacent)
            cc += 1
    return cc


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
    visited = [False]*len(adj)
    cc = 0
    print(number_of_components(adj))
