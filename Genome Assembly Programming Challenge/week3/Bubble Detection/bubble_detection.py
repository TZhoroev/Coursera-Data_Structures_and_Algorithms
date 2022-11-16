# python3
import sys
import itertools
from collections import defaultdict


def pre_process():
    data = sys.stdin.read().strip().split()
    k, t, reads = int(data[0]), int(data[1]), data[2:]
    kmers = [kmer for read in reads for kmer in [read[j:j + k] for j in range(len(read) - k + 1)]]
    return t, build_deBruijn_graph(kmers)


def build_deBruijn_graph(kmers):
    graph = defaultdict(lambda: [set(), 0])
    for kmer in kmers:
        prefix, suffix = kmer[:-1], kmer[1:]
        if prefix != suffix:
            if suffix not in graph[prefix][0]:
                graph[prefix][0].add(suffix)
                graph[suffix][1] += 1
    return graph


def count_bubbles(t, graph):
    bubbles = 0
    paths = defaultdict(lambda: list())

    def dfs(path, start, current, depth):
        if current != start and graph[current][1] > 1: paths[(start, current)].append(path[:])
        if depth == t: return
        for next_node in graph[current][0]:
            if next_node not in path:
                path.append(next_node)
                dfs(path, start, next_node, depth + 1)
                path.remove(next_node)

    for node in graph.keys():
        if len(graph[node][0]) > 1: dfs(path=[node], start=node, current=node, depth=0)
    for path_list in paths.values():
        for pair in itertools.combinations(path_list, r=2):
            if len(set(pair[0]) & set(pair[1])) == 2: bubbles += 1
    return bubbles


def Solution():
    t, graph = pre_process()
    print(count_bubbles(t, graph))


if __name__ == "__main__":
    Solution()
