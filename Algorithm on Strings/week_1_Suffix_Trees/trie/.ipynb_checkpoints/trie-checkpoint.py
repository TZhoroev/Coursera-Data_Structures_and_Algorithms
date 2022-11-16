#  python3

import sys
from collections import defaultdict

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.


def build_trie(patterns):
    trie = defaultdict(lambda: {})
    total = 1
    for pattern in patterns:
        current_node = 0
        for symbol in pattern:
            if symbol in trie[current_node].keys():
                current_node = trie[current_node][symbol]
            else:
                trie[current_node][symbol] = total
                current_node = total
                total += 1
    return trie


if __name__ == '__main__':
    pattern_s = sys.stdin.read().split()[1:]
    tree = build_trie(pattern_s)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))
