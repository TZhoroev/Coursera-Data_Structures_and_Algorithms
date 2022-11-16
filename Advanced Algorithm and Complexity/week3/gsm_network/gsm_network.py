# python3
import itertools


def varnum(i, k):
    return 3 * (i - 1) + k


def exactlyOneOf(i, colors, clauses):
    literals = [varnum(i, k) for k in colors]
    clauses.append(literals)
    for pair in itertools.combinations(literals, 2):
        clauses.append([-l for l in pair])
    return clauses


def adj(i, j, colors, clauses):
    for k in colors:
        clauses.append([-varnum(i, k), -varnum(j, k)])
    return clauses


def Solution(n, edges):
    clauses = []
    colors = range(1, 4)
    for index in range(1, n + 1):
        clauses = exactlyOneOf(index, colors, clauses)
    for i, j in edges:
        clauses = adj(i, j, colors, clauses)
    return clauses


if __name__ == '__main__':
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for i in range(m)]
    clauses = Solution(n, edges)
    print(len(clauses), n * 3)
    for c in clauses:
        c.append(0)
        print(' '.join(map(str, c)))
