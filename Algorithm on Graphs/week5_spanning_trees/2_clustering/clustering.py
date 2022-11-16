import sys
import math


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

    def NumClusters(self):
        return len(set(self.parent.values()))


def clustering(x_coord, y_coord, k_idx, n_len):
    weights = []
    for i in range(n_len):
        for j in range(i + 1, n_len):
            weights.append((math.sqrt((x_coord[i] - x_coord[j])**2 + (y_coord[i] - y_coord[j])**2), i, j))
    weights.sort(key=lambda item: item[0], reverse=True)
    vertices = set()
    belong_set = DisjointSet(n_len)
    edges = 0
    while edges <= n_len - k_idx:
        weight_uv, u, v = weights.pop()
        bu = belong_set.Find(u)
        bv = belong_set.Find(v)
        if bu != bv:
            if edges == (n_len - k_idx): return weight_uv
            vertices.update([u, v])
            belong_set.Union(bu, bv)
            edges += 1


if __name__ == '__main__':
    inputs = sys.stdin.read()
    data = list(map(int, inputs.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k, n)))
