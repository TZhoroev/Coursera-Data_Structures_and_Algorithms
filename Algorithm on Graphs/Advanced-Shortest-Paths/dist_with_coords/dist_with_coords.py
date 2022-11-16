import sys
from heapq import heappop, heappush
from collections import defaultdict
import math


class AStar:
    def __init__(self, n, adjacency, costs, x_coord, y_coord):
        # See the explanations of these fields in the starter for friend_suggestion        
        self.n = n
        self.adj = adjacency
        self.cost = costs
        self.inf = n * 10 ** 6
        self.d = defaultdict(lambda: self.inf)
        self.visited = defaultdict(lambda: False)
        self.work_set = set()  # open_list
        self.x = x_coord
        self.y = y_coord
        self.prior = {}

    def clear(self):
        self.d = defaultdict(lambda: self.inf)
        self.visited = defaultdict(lambda: False)
        self.work_set = set()
        self.prior = {}

    def visit(self, q, node_v, dist, prior_len):
        if self.d[node_v] > dist:
            self.d[node_v] = dist
            heappush(q, (dist + prior_len, node_v))
            self.work_set.add(node_v)

    def potential(self, u_node, target_node):
        if u_node not in self.prior:
            u_node = (self.x[u_node], self.y[u_node])
            target_node = (self.x[target_node], self.y[target_node])
            self.prior[u_node] = math.hypot(u_node[0]-target_node[0], u_node[1]-target_node[1])
        return self.prior[u_node]

    def process(self, q, v_node, target_node):
        for u_node, weight in zip(self.adj[v_node], self.cost[v_node]):
            if not self.visited[u_node]:
                self.visit(q, u_node, self.d[v_node] + weight, self.potential(u_node, target_node))

    def query(self, start, target):
        self.clear()
        q = []
        self.visit(q, start, 0, self.potential(start, target))
        while q:
            weight, v_node = heappop(q)
            if v_node == target:
                return self.d[target] if self.d[target] != self.inf else -1
            if not self.visited[v_node]:
                self.process(q, v_node, target)
                self.visited[v_node] = True
        return -1


def read_line():
    return map(int, sys.stdin.readline().split())


if __name__ == '__main__':
    n, m = read_line()
    x = [0 for _ in range(n)]
    y = [0 for _ in range(n)]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for i in range(n):
        a, b = read_line()
        x[i] = a
        y[i] = b
    for e in range(m):
        u, v, c = read_line()
        adj[u-1].append(v-1)
        cost[u-1].append(c)
    t, = read_line()
    astar = AStar(n, adj, cost, x, y)
    for i in range(t):
        s, t = read_line()
        print(astar.query(s-1, t-1))
