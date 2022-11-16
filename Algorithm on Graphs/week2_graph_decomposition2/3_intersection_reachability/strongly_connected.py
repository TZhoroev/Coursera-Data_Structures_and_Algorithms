#Uses python3

import sys

sys.setrecursionlimit(2000000)


def explore(v, adjacent, visited,  post):
    global clock
    visited[v] = True
    for w in adjacent[v]:
        if not visited[w]:
            explore(w, adjacent, visited, post)
    post[v] = clock
    clock += 1

def explore_bs(v, adjacent, visited):
    global clock
    visited[v] = True
    for w in adjacent[v]:
        if not visited[w]:
            explore_bs(w, adjacent, visited)

def dfs(edge, visited):
    global clock
    post = [0] * len(edge)
    for v in range(len(edge)):
        if not visited[v]:
            explore(v, edge, visited, post)
    return post


def number_of_strongly_connected_components(edge, reversed_adj):
    visited = [False] * len(edge)
    post = dfs(reversed_adj, visited)
    visited = [False] * len(edge)
    post = list(enumerate(post))
    post.sort(key=lambda x: x[1], reverse=True)
    orders = [item[0] for item in post]
    result = 0
    for v in orders:
        if not visited[v]:
            explore_bs(v, edge, visited)
            result += 1
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    reverse_adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        reverse_adj[b-1].append(a - 1)
    clock = 1
    print(number_of_strongly_connected_components(adj, reverse_adj))
