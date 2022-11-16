# python3
from itertools import combinations
from collections import deque, defaultdict
INF = 10 ** 9


def read_data():
    n, m = map(int, input().split())
    graph = [[INF] * n for _ in range(n)]
    for _ in range(m):
        u, v, weight = map(int, input().split())
        u -= 1
        v -= 1
        graph[u][v] = graph[v][u] = weight
    return graph


def print_answer(path_weight, path):
    print(path_weight)
    if path_weight == -1:
        return
    print(' '.join(map(str, path)))


def optimal_path(graph):
    n = len(graph)
    C = defaultdict(lambda: defaultdict(lambda: INF))
    backtrack = defaultdict(lambda: defaultdict(lambda: (-1, -1)))
    C[1][0] = 0
    for size in range(1, n):
        for S in combinations(range(n), size):
            S = (0,) + S
            k = sum([1 << i for i in S])
            for i in S:
                if i != 0:
                    for j in S:
                        if j != i:
                            curr = C[k ^ (1 << i)][j] + graph[i][j]
                            if curr < C[k][i]:
                                C[k][i] = curr
                                backtrack[k][i] = (k ^ (1 << i), j)

    path_weight, curr_index2 = min([(C[(1 << n) - 1][i] + graph[0][i], i) for i in range(n)])
    if path_weight >= INF: return -1, []
    best_path = deque()
    curr_index1 = (1 << n) - 1
    while curr_index1 != -1:
        best_path.appendleft(curr_index2 + 1)
        curr_index1, curr_index2 = backtrack[curr_index1][curr_index2]
    return path_weight, best_path


if __name__ == '__main__':
    print_answer(*optimal_path(read_data()))
