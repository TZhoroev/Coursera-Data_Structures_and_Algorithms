import sys
import math as math


class DisjointSet:
    def __init__(self, n_nodes):
        self.parent = {i: i for i in range(n_nodes)}
        self.rank = [0] * n_nodes

    def Find(self, i):
        if i != self.parent[i]:
            self.parent[i] = self.Find(self.parent[i])
        return self.parent[i]

    def Union(self, i, j):
        # i_parent = self.Find(i)
        # j_parent = self.Find(j)
        i_parent = i
        j_parent = j  # only for this problem otherwise use above
        if i_parent == j_parent:
            return
        else:
            if self.rank[i_parent] > self.rank[j_parent]:
                self.parent[j_parent] = i_parent
            else:
                self.parent[i_parent] = j_parent
                if self.rank[i_parent] == self.rank[j_parent]:
                    self.rank[j_parent] += 1


def minimum_distance(x_coord, y_coord, n_len):
    weights = []
    for i in range(n_len):
        for j in range(i + 1, n_len):
            weights.append((math.sqrt((x_coord[i] - x_coord[j])**2 + (y_coord[i] - y_coord[j])**2), i, j))
    weights.sort(key=lambda item: item[0], reverse=True)
    vertices = set()
    belong_set = DisjointSet(n_len)
    result = 0
    edges = 0
    while edges != n_len - 1:
        weight_uv, u, v = weights.pop()
        bu = belong_set.Find(u)
        bv = belong_set.Find(v)
        if bu != bv:
            vertices.update([u, v])
            belong_set.Union(bu, bv)
            result += weight_uv
            edges += 1
    return result


if __name__ == '__main__':
    inputs = sys.stdin.read()
    data = list(map(int, inputs.split()))
    # data = [5, 0, 0, 0, 2, 1, 1, 3, 0, 3, 2]
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y, n)))


