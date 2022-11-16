import sys
from heapq import heappop, heappush
from collections import defaultdict


class BiDij:
    def __init__(self, num_nodes):
        self.n = num_nodes                            # Number of nodes
        self.inf = 10 ** 6                      # All distances in the graph are smaller
        self.d = [defaultdict(lambda: self.inf), defaultdict(lambda: self.inf)]   # Initialize distances for forward and backward searches
        self.visited = defaultdict(lambda: False)           # visited[v] == True iff v was visited by forward or backward search
        self.work_set = set()                       # All the nodes visited by forward or backward search

    def clear(self):
        #  Reinitialize the data structures for the next query after the previous query.
        self.d = [defaultdict(lambda: self.inf), defaultdict(lambda: self.inf)]
        self.visited = defaultdict(lambda: False)
        self.work_set = set()

    def visit(self, q, side, node_v, dist):
        if self.d[side][node_v] > dist:
            self.d[side][node_v] = dist
            heappush(q[side], (dist, node_v))
            self.work_set.add(node_v)

    def process(self, q, side, node_v, adjacency, costs):
        for u_node, w in zip(adjacency[node_v], costs[node_v]):
            self.visit(q, side, u_node, self.d[side][node_v] + w)

    def shortest_path(self):
        distance = self.inf
        for u_node in self.work_set:
            if self.d[0][u_node] + self.d[1][u_node] < distance:
                distance = self.d[0][u_node] + self.d[1][u_node]
        return distance if distance != self.inf else -1

    def query(self, adjacency, costs, start, end_t):
        self.clear()
        q = [[], []]
        self.visit(q, 0, start, 0)
        self.visit(q, 1, end_t, 0)
        while q[0] and q[1]:
            for side in [0, 1]:
                _, v_node = heappop(q[side])
                self.process(q, side, v_node, adjacency[side], costs[side])
                if self.visited[v_node]:
                    return self.shortest_path()
                self.visited[v_node] = True
        return -1


def read_line():
    return map(int, sys.stdin.readline().split())


if __name__ == '__main__':
    n, m = read_line()
    adj = [[[] for _ in range(n)], [[] for _ in range(n)]]
    cost = [[[] for _ in range(n)], [[] for _ in range(n)]]
    for e in range(m):
        u, v, c = read_line()
        adj[0][u-1].append(v-1)
        cost[0][u-1].append(c)
        adj[1][v-1].append(u-1)
        cost[1][v-1].append(c)
    t, = read_line()
    bi_dij = BiDij(n)
    for i in range(t):
        s, t = read_line()
        print(bi_dij.query(adj, cost, s-1, t-1))
