import sys
from heapq import heappush, heappop
from collections import defaultdict


class DistPreprocessLarge:
    def __init__(self, num_nodes, adjacency, costs):
        self.n = num_nodes
        self.INFINITY = num_nodes * 2 *(10 ** 6)
        self.adj = adjacency
        self.cost = costs
        self.bi_distance = [[self.INFINITY] * num_nodes, [self.INFINITY] * num_nodes]
        self.visited = defaultdict(lambda: False)
        self.work_set = set()
        self.q = []
        # Levels of nodes for node ordering heuristics
        self.level = [0] * num_nodes
        # Positions of nodes in the node ordering
        self.rank = [0] * num_nodes
        # Shortcut cover
        self.shortcut_cover = [0] * num_nodes
        count = 1

        for node_idx in range(num_nodes):  # Computing Heuristics for each node to get order
            heappush(self.q, (self.compute_importance(node_idx, False), node_idx))
        while self.q:
            _, node = heappop(self.q)
            importance = self.compute_importance(node)
            number_iteration = 0
            while self.q and (importance > self.q[0][0]) and (number_iteration < 100):
                number_iteration += 1
                heappush(self.q, (importance, node))
                _, node = heappop(self.q)
                importance = self.compute_importance(node)

            self.rank[node] = count
            count += 1
            self.visited[node] = True
            if self.adj[0][node]:
                for v_node in range(len(self.adj[1][node])):
                    check = max(self.cost[1][node]) + max(self.cost[0][node])  # Set a check value that is the current path cost being checked
                    to_add = []  # Array to store edges to add
                    self.witness(self.adj[1][node][v_node], self.cost[1][node][v_node], to_add, check, node)  # Check for witness edges, If no witness edge exists, mark points to add shortcuts
                    self.shortcut(to_add)  # Add Relevant Shortcuts

            for side, alter_side in enumerate([1, 0]):
                for node_idx in self.adj[side][node]:
                    target_idx = len(self.adj[alter_side][node_idx])
                    j_idx = 0
                    while j_idx < target_idx:
                        if self.adj[alter_side][node_idx][j_idx] == node:
                            self.adj[alter_side][node_idx][j_idx], self.adj[alter_side][node_idx][target_idx - 1] = self.adj[alter_side][node_idx][target_idx - 1], self.adj[alter_side][node_idx][j_idx]
                            self.cost[alter_side][node_idx][j_idx], self.cost[alter_side][node_idx][target_idx - 1] = self.cost[alter_side][node_idx][target_idx - 1], self.cost[alter_side][node_idx][j_idx]
                            self.adj[alter_side][node_idx].pop()
                            self.cost[alter_side][node_idx].pop()
                            target_idx -= 1
                            break
                        else:
                            j_idx += 1

        self.visited = defaultdict(lambda: None)

    def compute_importance(self, v_node, consider_n=True):
        neighbors = 0
        if consider_n:
            for node_idx in self.adj[0][v_node] + self.adj[1][v_node]:
                self.level[node_idx] = max(self.level[v_node] + 1, self.level[node_idx])
                if self.visited[node_idx]:
                    neighbors += 1
        return ((len(self.adj[0][v_node]) * len(self.adj[1][v_node])) - len(self.adj[0][v_node]) - len(self.adj[1][v_node]) + neighbors +
                self.shortcut_cover[v_node] + self.level[v_node])

        # contraction node
    def shortcut(self, to_add):
        for u_node, v_node, cost_uv in to_add:
            self.add_arc(u_node, v_node, cost_uv)

    def add_arc(self, u_node, v_node, cost_uv):  # Add a shortcut from node u to v
        self.shortcut_cover[u_node] += 1
        self.shortcut_cover[v_node] += 1
        update(self.adj[0], self.cost[0], u_node, v_node, cost_uv)
        update(self.adj[1], self.cost[1], v_node, u_node, cost_uv)

    def witness(self, start, cost_s, to_add, check, v_node):  # Perform regular Dijkstra with some modifications
        dist = self.bi_distance[0]  # Distance to each node from source
        traveled = set()  # If node has been processed before
        dist[start] = 0  # Source node distance = 0
        self.work_set.add(start)
        heap_pq = [(dist[start], start)]  # Priority queue initialized with source node
        count = 0  # Stop Dijkstra optimization to specify threshold
        while heap_pq and (count < 6):
            count += 1
            _, node_idx = heappop(heap_pq)  # Pick topmost Item and check if it has been processed already
            while heap_pq and (node_idx in traveled):
                _, node_idx = heappop(heap_pq)
            if not heap_pq and (node_idx in traveled):
                break
            traveled.add(node_idx)
            for adj_idx in range(len(self.adj[0][
                                   node_idx])):  # Check neighbors if node can be relaxed, while also checking if path length is already over the current path being witnessed. Avoid node being relaxed v
                if (self.adj[0][node_idx][adj_idx] != v_node) and (
                        dist[self.adj[0][node_idx][adj_idx]] > dist[node_idx] + self.cost[0][node_idx][adj_idx]) and (
                        dist[node_idx] + self.cost[0][node_idx][adj_idx] < check):
                    self.work_set.add(self.adj[0][node_idx][adj_idx])
                    dist[self.adj[0][node_idx][adj_idx]] = dist[node_idx] + self.cost[0][node_idx][adj_idx]
                    heappush(heap_pq, (dist[self.adj[0][node_idx][adj_idx]], self.adj[0][node_idx][adj_idx]))

        for target_idx in range(len(self.adj[0][v_node])):
            if dist[self.adj[0][v_node][target_idx]] > cost_s + self.cost[0][v_node][target_idx]:
                to_add.append((start, self.adj[0][v_node][target_idx], cost_s + self.cost[0][v_node][target_idx]))

        for adj_idx in self.work_set:
            dist[adj_idx] = self.INFINITY
        self.work_set.clear()

    def mark_visited(self, node, side):
        if self.visited[node] is None:
            self.visited[node] = side
        elif self.visited[node] == (1 - side):
            self.visited[node] = 2

    def clear(self):
        for node_v in self.work_set:
            self.bi_distance[0][node_v] = self.bi_distance[1][node_v] = self.INFINITY
            self.visited[node_v] = None
        self.work_set.clear()

    def visit(self, q, side, index):
        self.mark_visited(index, side)
        for node_v in range(len(self.adj[side][index])):
            self.work_set.add(self.adj[side][index][node_v])
            if self.bi_distance[side][self.adj[side][index][node_v]] > self.bi_distance[side][index] + \
                    self.cost[side][index][node_v]:
                self.bi_distance[side][self.adj[side][index][node_v]] = self.bi_distance[side][index] + \
                                                                        self.cost[side][index][node_v]
                heappush(q[side], (self.bi_distance[side][self.adj[side][index][node_v]], self.adj[side][index][node_v]))

    def query(self, start_node, target_node):  # bi_directional Dijkstra
        self.clear()
        estimate = self.INFINITY
        heap_pq = [[], []]
        self.bi_distance[0][start_node] = 0
        self.bi_distance[1][target_node] = 0
        self.work_set.add(start_node)
        self.work_set.add(target_node)
        heappush(heap_pq[0], (self.bi_distance[0][start_node], start_node))
        heappush(heap_pq[1], (self.bi_distance[1][target_node], target_node))
        while heap_pq[0] or heap_pq[1]:
            if heap_pq[0]:
                _, node_idx = heappop(heap_pq[0])
                while heap_pq[0] and ((self.visited[node_idx] == 0) or (self.visited[node_idx] == 2)):
                    _, node_idx = heappop(heap_pq[0])
                if self.bi_distance[0][node_idx] <= estimate:
                    self.visit(heap_pq, 0, node_idx)
                if estimate > self.bi_distance[0][node_idx] + self.bi_distance[1][node_idx]:
                    estimate = self.bi_distance[0][node_idx] + self.bi_distance[1][node_idx]

            if heap_pq[1]:
                _, reverse_idx = heappop(heap_pq[1])
                while heap_pq[1] and ((self.visited[reverse_idx] == 1) or (self.visited[reverse_idx] == 2)):
                    _, reverse_idx = heappop(heap_pq[1])
                if self.bi_distance[1][reverse_idx] <= estimate:
                    self.visit(heap_pq, 1, reverse_idx)
                if estimate > self.bi_distance[0][reverse_idx] + self.bi_distance[1][reverse_idx]:
                    estimate = self.bi_distance[0][reverse_idx] + self.bi_distance[1][reverse_idx]

        return -1 if estimate == self.INFINITY else estimate


def update(adjacency, weights, u_node, v_node, cost_uv):
    for node_idx in range(len(adjacency[u_node])):
        if adjacency[u_node][node_idx] == v_node:
            weights[u_node][node_idx] = min(weights[u_node][node_idx], cost_uv)
            return
    adjacency[u_node].append(v_node)
    weights[u_node].append(cost_uv)


def read_line():
    return map(int, sys.stdin.readline().split())


if __name__ == '__main__':
    n, m = read_line()
    adj = [[[] for _ in range(n)], [[] for _ in range(n)]]
    cost = [[[] for _ in range(n)], [[] for _ in range(n)]]
    for e in range(m):
        u, v, c = read_line()
        adj[0][u - 1].append(v - 1)
        cost[0][u - 1].append(c)
        adj[1][v - 1].append(u - 1)
        cost[1][v - 1].append(c)

    ch = DistPreprocessLarge(n, adj, cost)
    print("Ready")
    sys.stdout.flush()
    t, = read_line()
    for i in range(t):
        s, t = read_line()
        print(ch.query(s - 1, t - 1))
