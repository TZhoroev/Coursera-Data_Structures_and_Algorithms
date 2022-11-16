# python3
import itertools


def varnum(i, j):
    return n*i + j


def exactlyOneOf(literals, clauses):
    clauses.append(literals)
    for pair in itertools.combinations(literals, 2):
        clauses.append([-l for l in pair])
    return clauses


def Solution(n, edges):
    clauses = []
    positions = range(1, n+1)
    adj = [[] for _ in range(n)]
    for i, j in edges:
        adj[i-1].append(j-1)
        adj[j-1].append(i-1)
    for i in range(n):
        clauses = exactlyOneOf([varnum(i, j) for j in positions], clauses)
    for j in positions:
        clauses = exactlyOneOf([varnum(i, j) for i in range(n)], clauses)
    for j in positions[:-1]:
        for i, nodes in enumerate(adj):
            clauses.append([-varnum(i, j)] + [varnum(node, j+1) for node in nodes])
    return clauses


if __name__ == '__main__':
    n, m = map(int, input().split())
    corridors = [list(map(int, input().split())) for item in range(m)]
    clause = Solution(n, corridors)
    print(len(clause), n*n)
    for c in clause:
        c.append(0)
        print(' '.join(map(str, c)))
