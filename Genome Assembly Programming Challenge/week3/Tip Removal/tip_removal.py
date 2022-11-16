# python3
import sys
from collections import defaultdict


def pre_process():
    reads = sys.stdin.read().strip().split()
    k = 15
    kmers = [kmer for read in reads for kmer in [read[j:j + k] for j in range(len(read) - k + 1)]]
    return build_deBruijn_graph(kmers)


def build_deBruijn_graph(kmers):
    graph = defaultdict(lambda: [set(), 0])
    for kmer in kmers:
        prefix, suffix = kmer[:-1], kmer[1:]
        if prefix != suffix:
            if suffix not in graph[prefix][0]:
                graph[prefix][0].add(suffix)
                graph[suffix][1] += 1
    return graph


def tips_removal(graph):
    n_edges_removed = 0
    for value in graph.values():
        if len(value[0]) == 1 and value[1] == 0: find_and_remove = remove_incoming
        elif len(value[0]) > 1: find_and_remove = remove_outgoing
        else: continue
        condition = True
        while condition:
            condition = False
            for edge in value[0]:
                removed, graph, n_edges_removed = find_and_remove(edge, 0, graph, n_edges_removed)
                if removed:
                    value[0].remove(edge)
                    n_edges_removed += 1
                    condition = True
                    break
    return n_edges_removed


def remove_outgoing(current, depth, graph, n_edges_removed):
    k = 15
    if len(graph[current][0]) > 1 or graph[current][1] > 1 or depth == k: return False, graph, n_edges_removed
    elif len(graph[current][0]) == 0: return True, graph, n_edges_removed
    removed, graph, n_edges_removed = remove_outgoing(next(iter(graph[current][0])), depth + 1, graph,
                                                      n_edges_removed)
    if removed:
        graph[current][0].pop()
        n_edges_removed += 1
        return True, graph, n_edges_removed
    return False, graph, n_edges_removed


def remove_incoming(current, depth, graph, n_edges_removed):
    k = 15
    if depth == k: return False, graph, n_edges_removed
    if len(graph[current][0]) == 0 or graph[current][1] > 1: return True, graph, n_edges_removed
    removed, graph, n_edges_removed = remove_incoming(next(iter(graph[current][0])), depth + 1, graph,
                                                      n_edges_removed)
    if removed:
        graph[current][0].pop()
        n_edges_removed += 1
        return True, graph, n_edges_removed
    return False, graph, n_edges_removed


def Solution():
    graph = pre_process()
    print(tips_removal(graph))


if __name__ == "__main__":
    Solution()
