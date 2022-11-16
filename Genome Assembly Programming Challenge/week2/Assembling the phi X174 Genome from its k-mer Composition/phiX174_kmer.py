# python3
import sys


class EulerianCycle:
    def __init__(self, adj):
        self.graph = adj
        self.n = len(self.graph)
        self.m = 0
        self.unused_node = dict()
        self.in_deg = dict()
        self.out_deg = dict()
        self.adj_position = dict()
        self.path = []
        self.updateAdj()

    def updateAdj(self):
        for w, vList in self.graph.items():
            self.in_deg[w] = self.in_deg.get(w, 0)
            for v in vList:
                self.in_deg[v] = self.in_deg.get(v, 0) + 1
            l = len(vList)
            self.out_deg[w] = l
            self.m += l
            self.adj_position[w] = 0

    def explore_node(self, node):
        self.path.append(node)
        cur_pos, max_pos = self.adj_position[node], self.out_deg[node]
        while cur_pos < max_pos:
            self.adj_position[node] = cur_pos + 1
            if cur_pos + 1 < max_pos: self.unused_node[node] = len(self.path) - 1
            else:
                if node in self.unused_node: del self.unused_node[node]
            node = self.graph[node][cur_pos]
            self.path.append(node)
            cur_pos, max_pos = self.adj_position[node], self.out_deg[node]
            self.m -= 1
        return

    def update_path(self, start_pos):
        l = len(self.path) - 1
        self.path = self.path[start_pos:l] + self.path[:start_pos]
        for node, pos in self.unused_node.items():
            if pos < start_pos: self.unused_node[node] = pos + l - start_pos
            else: self.unused_node[node] = pos - start_pos
        return

    def find_euler_cycle(self):
        w, vList = self.graph.popitem()
        self.graph[w] = vList
        self.explore_node(w)
        while self.m > 0:
            node, pos = self.unused_node.popitem()
            self.update_path(pos)
            self.explore_node(node)
        return self.path


def genome_from_path(path):
    return path[0] + ''.join(seq[-1] for seq in path[1:])


def De_Brujin(k, patterns):
    adj = dict()
    for p in patterns:
        if p[:k - 1] in adj:
            adj[p[:k - 1]].append(p[1:])
        else:
            adj[p[:k - 1]] = []
            adj[p[:k - 1]].append(p[1:])
        if p[1:] not in adj: adj[p[1:]] = []
    return adj


def readData():
    data = list(sys.stdin.read().strip().split())
    # data = ["ATGC", "ATGG", "TGCC", "GCCA", "CCAT", "CATG","GATG", "TGGG","GGGA", "GGAT"]
    adj = De_Brujin(len(data[0]), data)
    return len(data[0]), adj


def Solution():
    k, adj = readData()
    path = EulerianCycle(adj).find_euler_cycle()
    print(genome_from_path(path)[:-k + 1])


if __name__ == "__main__":
    Solution()
