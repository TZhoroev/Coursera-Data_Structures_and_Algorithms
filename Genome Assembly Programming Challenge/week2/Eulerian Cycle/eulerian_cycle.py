# python3
import sys
from collections import defaultdict


def pre_process():
    data = list(sys.stdin.read().strip().split())
    n, m = int(data[0]), int(data[1])
    graph = defaultdict(lambda: [])
    out_deg = [0] * n
    in_deg = [0] * n
    for i in range(m):
        node_a = int(data[2 * i + 2]) - 1
        node_b = int(data[2 * i + 3]) - 1
        graph[node_a].append(node_b)
        out_deg[node_a] += 1
        in_deg[node_b] += 1
    return out_deg == in_deg, n, m, out_deg, graph


def explore_node(graph, path, node, adj_position, out_deg, unused_node, m):
    path.append(node)
    cur_pos, max_pos = adj_position[node], out_deg[node]
    while cur_pos < max_pos:
        adj_position[node] = cur_pos + 1
        if cur_pos + 1 < max_pos: unused_node[node] = len(path) - 1
        elif node in unused_node: del unused_node[node]
        node = graph[node][cur_pos]
        path.append(node)
        cur_pos, max_pos = adj_position[node], out_deg[node]
        m -= 1
    return m, path, unused_node, adj_position


def update_path(path, unused_node, start_pos):
    l = len(path) - 1
    path = path[start_pos:l] + path[:start_pos]
    for node, pos in unused_node.items():
        if pos < start_pos: unused_node[node] = pos + l - start_pos
        else: unused_node[node] = pos - start_pos
    return path, unused_node


def find_euler_cycle(n, m, out_deg, graph):
    unused_node = dict()
    adj_position = [0] * n
    path = []
    m, path, unused_node, adj_position = explore_node(graph, path, 1, adj_position, out_deg, unused_node, m)
    while m > 0:
        node, pos = unused_node.popitem()
        path, unused_node = update_path(path, unused_node, pos)
        m, path, unused_node, adj_position = explore_node(graph, path, node, adj_position, out_deg, unused_node, m)
    return path


def print_euler_path(path):
    print(' '.join([str(node + 1) for node in path[:-1]]))


def Solution():
    is_balanced, n, m, out_deg, graph = pre_process()
    if not is_balanced:
        print("0")
    else:
        print("1")
        print_euler_path(find_euler_cycle(n, m, out_deg, graph))


if __name__ == "__main__":
    Solution()
