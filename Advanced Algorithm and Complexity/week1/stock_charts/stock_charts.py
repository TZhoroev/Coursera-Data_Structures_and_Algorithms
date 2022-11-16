# python3
from collections import defaultdict
from heapq import heappop, heappush


def write_response(result):
    print(result)


class StockCharts:
    def __init__(self):
        self.adj_matrix = None
        self.busy_right = None
        self.matching = None
        n, _ = map(int, input().split())
        self.n = n
        stock_data = [list(map(int, input().split())) for i in range(n)]
        self.stock_data = stock_data

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
                for j in range(self.n):
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

    def min_charts(self):
        self.matching = [-1] * self.n
        self.busy_right = [False] * self.n
        self.adj_matrix = [[0] * self.n for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                if all([x < y for x, y in zip(self.stock_data[i], self.stock_data[j])]):
                    self.adj_matrix[i][j] = 1
        while self.bfs():
            continue
        return sum([1 for i in self.matching if i == -1])

    def solve(self):
        matching = self.min_charts()
        write_response(matching)


if __name__ == '__main__':
    stock_charts = StockCharts()
    stock_charts.solve()

