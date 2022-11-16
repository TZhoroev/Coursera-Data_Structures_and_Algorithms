import sys
import math as math


class PriorityQueue:
    def __init__(self):
        self.array = []  # array to store binary heap
        self.label2idx = {}  # store labels
        self.total = 0

    # shift up method
    def shift_up(self, c):
        if c == 0: return  # current
        p = (c - 1) // 2  # index of parent
        if self.array[p][1] > self.array[c][1]:
            self.array[c], self.array[p] = self.array[p], self.array[c]
            self.label2idx[self.array[c][0]], self.label2idx[self.array[p][0]] = c, p
            self.shift_up(p)

    def shift_down(self, p):
        if p >= len(self.array): return
        l, r = 2 * p + 1, 2 * p + 2
        if l >= len(self.array): l = p
        if r >= len(self.array): r = p
        c = l if self.array[r][1] > self.array[l][1] else r
        if self.array[p][1] > self.array[c][1]:
            self.array[c], self.array[p] = self.array[p], self.array[c]
            self.label2idx[self.array[c][0]], self.label2idx[self.array[p][0]] = c, p
            self.shift_down(c)

    def insert(self, label, key):
        self.array.append([label, key])
        idx = len(self.array) - 1
        self.label2idx[self.array[idx][0]] = idx
        self.shift_up(idx)
        self.total += 1

    def pop_min(self):
        if self.total == 0: return "NO ELEMENT"
        self.array[0], self.array[-1] = self.array[-1], self.array[0]
        self.label2idx[self.array[0][0]] = 0
        del self.label2idx[self.array[-1][0]]
        min_label = self.array.pop()[0]
        self.shift_down(0)
        self.total -= 1
        return min_label

    def change_priority(self, label, key):
        if label in self.label2idx:
            idx = self.label2idx[label]
            if key < self.array[idx][1]:
                self.array[idx][1] = key
                self.shift_up(idx)

    def build_heap(self, a_array):
        self.array =[[label, key] for label, key in enumerate(a_array)]
        self.label2idx = {label: label for label, _ in enumerate(a_array)}
        len_a = len(a_array)
        self.total = len_a
        for i in range(len_a//2-1, -1, -1):
            self.shift_down(i)


def minimum_distance(x_coord, y_coord, n_len):
    weights = [[0 for _ in range(n_len)] for _ in range(n_len)]
    for i in range(n_len):
        for j in range(i + 1, n_len):
            weights[i][j] = weights[j][i] = math.sqrt((x_coord[i] - x_coord[j])**2 + (y_coord[i] - y_coord[j])**2)
    cost = [float("inf")] * n_len
    parent = [None] * n_len
    cost[0] = 0
    visited = [False]*n
    prio_q = PriorityQueue()
    prio_q.build_heap(cost)
    while prio_q.total:
        v = prio_q.pop_min()
        visited[v] = True
        for z, weight in enumerate(weights[v]):
            if z == v or visited[z]:
                continue
            if cost[z] > weight:
                cost[z] = weight
                parent[z] = v
                prio_q.change_priority(z, weight)
    result = 0
    for i in range(n_len):
        if parent[i] is not None:
            result += weights[i][parent[i]]
    return result


if __name__ == '__main__':
    inputs = sys.stdin.read()
    data = list(map(int, inputs.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y, n)))


