# python3
from collections import defaultdict
from heapq import heappop, heappush


def write_response(matching):
    line = [str(-1 if x == -1 else x + 1) for x in matching]
    print(' '.join(line))


class MaxMatching:
    def __init__(self):
        self.busy_right = None
        self.matching = None
        self.m = None
        self.n = None
        n, m = map(int, input().split())
        adj_matrix = [list(map(int, input().split())) for i in range(n)]
        self.adj_matrix = adj_matrix

    def bfs(self):
        nodes = []
        heappush(nodes, (0, None))
        path = []
        prev = defaultdict(lambda: (0, None))
        visited_nodes = set()
        visited_nodes.add((0, None))
        while nodes:
            curr_node = heappop(nodes)
            if curr_node[0] == 0:
                for i in range(self.n):
                    if self.matching[i] == -1:
                        visited_nodes.add((1, i))
                        prev[(1, i)] = (0, None)
                        heappush(nodes, (1, i))
            elif curr_node[0] == 1:
                i = curr_node[1]
                for j in range(self.m):
                    if self.adj_matrix[i][j] == 1 and self.matching[i] != j and (2, j) not in visited_nodes:
                        visited_nodes.add((2, j))
                        prev[(2, j)] = curr_node
                        heappush(nodes, (2, j))
            elif curr_node[0] == 2:
                j = curr_node[1]
                if not self.busy_right[j]:
                    prev_node = curr_node
                    curr_node = (3, j)
                    while True:
                        path.insert(0, (prev_node, curr_node))
                        if prev_node[0] == 0:
                            break
                        curr_node = prev_node
                        prev_node = prev[curr_node]
                    for edge in path:
                        if edge[0][0] == 1:
                            self.matching[edge[0][1]] = edge[1][1]
                        elif edge[0][0] == 2 and edge[1][0] == 3:
                            self.busy_right[edge[1][1]] = True
                    return True
                else:
                    for i in range(self.n):
                        if j == self.matching[i] and (1, i) not in visited_nodes:
                            visited_nodes.add((1, i))
                            prev[(1, i)] = curr_node
                            heappush(nodes, (1, i))
        return False

    def find_matching(self):
        self.n = len(self.adj_matrix)
        self.m = len(self.adj_matrix[0])
        self.matching = [-1] * self.n
        self.busy_right = [False] * self.m
        while self.bfs():
            continue
        return self.matching

    def solve(self):
        matching = self.find_matching()
        write_response(matching)


if __name__ == '__main__':
    max_matching = MaxMatching()
    max_matching.solve()
