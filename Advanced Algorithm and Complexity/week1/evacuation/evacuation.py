# python3
from collections import defaultdict
from heapq import heappop, heappush

class Edge:

    def __init__(self, u, v, capacity):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.flow = 0


# This class implements a bit unusual scheme for storing edges of the graph,
# in order to retrieve the backward edge for a given edge quickly.
class FlowGraph:

    def __init__(self, n):
        # List of all - forward and backward - edges
        self.edges = []
        # These adjacency lists store only indices of edges in the edges list
        self.graph = [[] for _ in range(n)]

    def add_edge(self, from_, to, capacity):
        # Note that we first append a forward edge and then a backward edge,
        # so all forward edges are stored at even indices (starting from 0),
        # whereas backward edges are stored at odd indices.
        forward_edge = Edge(from_, to, capacity)
        backward_edge = Edge(to, from_, 0)
        self.graph[from_].append(len(self.edges))
        self.edges.append(forward_edge)
        self.graph[to].append(len(self.edges))
        self.edges.append(backward_edge)

    def size(self):
        return len(self.graph)

    def get_ids(self, from_):
        return self.graph[from_]

    def get_edge(self, id):
        return self.edges[id]

    def add_flow(self, id, flow):
        # To get a backward edge for a true forward edge (i.e id is even), we should get id + 1
        # due to the described above scheme. On the other hand, when we have to get a "backward"
        # edge for a backward edge (i.e. get a forward edge for backward - id is odd), id - 1
        # should be taken.
        #
        # It turns out that id ^ 1 works for both cases. Think this through!
        self.edges[id].flow += flow
        self.edges[id ^ 1].flow -= flow
        self.edges[id].capacity -= flow
        self.edges[id ^ 1].capacity += flow


def read_data():
    vertex_count, edge_count = map(int, input().split())
    graph = FlowGraph(vertex_count)
    for _ in range(edge_count):
        u, v, capacity = map(int, input().split())
        graph.add_edge(u - 1, v - 1, capacity)
    return graph


def bfs(graph, from_, to):
    # modified version of the bfs, it returns if path exist and path and weight of the path.
    weight = float('inf')
    dist = defaultdict(lambda: float('inf'))
    dist[from_] = 0
    prev = defaultdict(lambda: (None, None))
    path = []
    nodes = []
    heappush(nodes, (0, from_))
    while nodes:
        _, curr_node = heappop(nodes)
        for id in graph.get_ids(curr_node):
            curr_edge = graph.get_edge(id)
            if float('inf') == dist[curr_edge.v] and curr_edge.capacity > 0:
                dist[curr_edge.v] = dist[curr_node] + 1
                prev[curr_edge.v] = (curr_node, id)
                heappush(nodes, (dist[curr_edge.v], curr_edge.v))
                if curr_edge.v == to:
                    while True:
                        path.insert(0, id)
                        curr_weight = graph.get_edge(id).capacity
                        weight = min(curr_weight, weight)
                        if curr_node == from_:
                            break
                        curr_node, id = prev[curr_node]
                    return True, path, weight
    return False, path, weight


def max_flow(graph, from_, to):
    flow = 0
    while True:
        path_exits, path, weight = bfs(graph, from_, to)
        if not path_exits:
            return flow
        for id in path:
            graph.add_flow(id, weight)
        flow += weight


if __name__ == '__main__':
    graphs = read_data()
    print(max_flow(graphs, 0, graphs.size() - 1))
