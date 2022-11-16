
import sys


def explore(v, adjacent, visited,  post):
    global clock
    visited[v] = True
    for w in adjacent[v]:
        if not visited[w]:
            explore(w, adjacent, visited, post)
    post[v] = clock
    clock += 1
    return post


def dfs(edge, visited):
    global clock
    post = [0] * len(edge)
    for v in range(len(edge)):
        if not visited[v]:
            post = explore(v, edge, visited, post)
    return post


def toposort(edge):
    visited = [False] * len(edge)
    post = dfs(edge, visited)
    post = list(enumerate(post))
    post.sort(key=lambda x: x[1], reverse=True)
    orders = [item[0] for item in post]
    return orders


if __name__ == '__main__':
    inputs = sys.stdin.read()
    data = list(map(int, inputs.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    clock = 1
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

