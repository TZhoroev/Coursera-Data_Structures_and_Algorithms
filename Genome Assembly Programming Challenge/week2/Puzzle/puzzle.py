# python3

import sys
from math import sqrt
from itertools import permutations
import pickle


def pre_process():
    # (up,left,down,right)
    data = sys.stdin.read().strip().split('\n')
    n = int(sqrt(len(data)))
    blocks = []
    for d in data:
        blocks.append(d[1:-1].split(','))
    return n, blocks


def process(n, blocks):
    edges = [[-1 for _ in range(n)] for __ in range(n)]
    borders = [[] for _ in range(4)]
    adj_edges = [[0 for _ in range(2)] for __ in range(4)]
    for i in range(len(blocks)):
        if blocks[i][0] == 'black':
            if 'black' == blocks[i][1]:
                edges[0][0] = i
                adj_edges[0][0] = i
                adj_edges[1][0] = i
            elif blocks[i][-1] == 'black':
                edges[0][-1] = i
                adj_edges[0][1] = i
                adj_edges[3][0] = i
            else:
                borders[0].append(i)
        elif blocks[i][2] == 'black':
            if blocks[i][1] == 'black':
                edges[-1][0] = i
                adj_edges[1][1] = i
                adj_edges[2][0] = i
            elif blocks[i][3] == 'black':
                edges[-1][-1] = i
                adj_edges[2][1] = i
                adj_edges[3][1] = i
            else:
                borders[2].append(i)
        elif blocks[i][1] == 'black':
            borders[1].append(i)
        elif 'black' == blocks[i][3]:
            borders[3].append(i)
    return edges, borders, adj_edges


def solve(n, blocks):
    edges, borders, adj_edge = process(n, blocks)
    adjacency = [(1, 3), (0, 2), (1, 3), (0, 2)]
    correction_index = [list(zip([0] * n, range(n))), list(zip(range(n), [0] * n)),
                        list(zip([n - 1] * n, range(n))), list(zip(range(n), [n - 1] * n))]
    for i in range(4):
        for p in permutations(borders[i]):
            p = [adj_edge[i][0]] + list(p) + [adj_edge[i][1]]
            isCorrect = True
            for j in range(len(p) - 1):
                if blocks[p[j]][adjacency[i][1]] != blocks[p[j + 1]][adjacency[i][0]]:
                    isCorrect = False
                    break
            if isCorrect:
                for j in range(len(p)):
                    edges[correction_index[i][j][0]][correction_index[i][j][1]] = p[j]
    correct = set()
    for a in edges:
        for i in a:
            if i != -1:
                correct.add(i)
    incorrect = [i for i in range(n ** 2) if i not in correct]

    index_mat1 = list(zip(sum([[i] * (n - 2) for i in range(1, n - 1)], []),
                          sum([list(range(1, n - 1)) for _ in range(n - 2)], [])))
    index_mat2 = [[(x[0] - 1, x[1], 2, 0), (x[0], x[1] - 1, 3, 1), (x[0] + 1, x[1], 0, 2), (x[0], x[1] + 1, 1, 3)] for x
                  in index_mat1]

    for p in permutations(incorrect):
        p = list(p)
        trial = pickle.loads(pickle.dumps(edges))
        for i in range(len(p)):
            trial[index_mat1[i][0]][index_mat1[i][1]] = p[i]
        isCorrect = True
        for i in range(len(p)):
            for j in range(4):
                if blocks[trial[index_mat2[i][j][0]][index_mat2[i][j][1]]][index_mat2[i][j][2]] != blocks[p[i]][index_mat2[i][j][3]]:
                    isCorrect = False
                    break
            if not isCorrect: break
        if isCorrect:
            edges = trial
            break
    return edges


def printResult(n, ans, block):
    for i in range(n):
        print(';'.join(['(' + ','.join(block[ans[i][j]]) + ')' for j in range(n)]))


def Solution():
    n, blocks = pre_process()
    ans = solve(n, blocks)
    printResult(n, ans, blocks)


if __name__ == "__main__":
    Solution()
