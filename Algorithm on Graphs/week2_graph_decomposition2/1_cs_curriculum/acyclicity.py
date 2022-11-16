
import sys


def explore(v, adjacent, visited, cycle):
    global dag
    visited[v] = True
    cycle.append(v)
    for w in adjacent[v]:
        if w in cycle:
            dag = False
        if not visited[w]:
            explore(w, adjacent, visited, cycle)
    cycle.pop()


def acyclic(adjacent):
    global dag
    visited = [False]*len(adjacent)
    cycle = []
    for v in range(len(adjacent)):
        if not visited[v]:
            explore(v, adjacent, visited, cycle)
            if not dag:
                return 1
    return 0


if __name__ == '__main__':
    inputs = sys.stdin.read()
    data = list(map(int, inputs.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    dag = True
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
