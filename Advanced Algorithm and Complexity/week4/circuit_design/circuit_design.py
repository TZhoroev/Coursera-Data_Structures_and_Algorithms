# python3
import sys
import threading

sys.setrecursionlimit(10 ** 7)
threading.stack_size(2**26)


def explore(adj, v, component_list, component_number):
    component_list[v] = component_number
    for w in adj[v]:
        if component_list[w] == 0: explore(adj, w, component_list, component_number)


def dfs(adj, v, visited, post, clock):
    visited[v] = True
    clock[0] += 1
    for w in adj[v]:
        if not visited[w]: dfs(adj, w, visited, post, clock)
    clock[0] += 1
    post[v] = clock[0]


def toposort(adj):
    clock = [0]
    visited = [False] * len(adj)
    post = [-1] * len(adj)
    for v in range(len(adj)):
        if not visited[v]: dfs(adj, v, visited, post, clock)
    order = list(range(len(post)))
    return sorted(order, key=lambda x: post[x], reverse=True)


def number_of_strongly_connected_components(adj, reverse_adj):
    top_order = toposort(reverse_adj)
    component_list = [0] * len(adj)
    component_number = 0
    for v in top_order:
        if component_list[v] == 0:
            component_number += 1
            explore(adj, v, component_list, component_number)
    return component_list, top_order


def node(x):
    return 2 * abs(x) - 1 - (x > 0)


def construct_G(n, clauses):
    adj = [[] for _ in range(2 * n)]
    reverse_adj = [[] for _ in range(2 * n)]
    for clause in clauses:
        adj[node(-clause[0])].append(node(clause[1]))
        adj[node(-clause[1])].append(node(clause[0]))
        reverse_adj[node(clause[1])].append(node(-clause[0]))
        reverse_adj[node(clause[0])].append(node(-clause[1]))
    return adj, reverse_adj


def isSatisfiable(n, clauses):
    adj, reverse_adj = construct_G(n, clauses)
    ssc_lst, top_order = number_of_strongly_connected_components(adj, reverse_adj)
    for i in range(n):
        if ssc_lst[2 * i] == ssc_lst[2 * i + 1]: return None
    assign = [-1] * (2 * n)
    for vertex in top_order:
        if assign[vertex] == -1:
            assign[vertex] = 1
            if vertex % 2 == 0: assign[vertex + 1] = 0
            else: assign[vertex - 1] = 0
    return [i if assign[2 * (i - 1)] else -i for i in range(1, n + 1)]


def main():
    n_vertex, m = map(int, sys.stdin.readline().strip().split())
    clause_list = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(m)]
    result = isSatisfiable(n_vertex, clause_list)
    if result is None:
        print("UNSATISFIABLE")
    else:
        print("SATISFIABLE")
        print(" ".join([str(x) for x in result]))


if __name__ == '__main__':
    threading.Thread(target=main).start()
