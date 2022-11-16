# python3
import sys


class SuffixTreeNode:
    def __init__(self, children, parent, stringDepth: int, edgeStart: int, edgeEnd: int):
        self.children = children
        self.parent = parent
        self.stringDepth = stringDepth
        self.edgeStart = edgeStart
        self.edgeEnd = edgeEnd


def create_new_leaf(node, string, suffix):
    leaf = SuffixTreeNode({}, node, len(string) - suffix, suffix + node.stringDepth, len(string)-1)
    node.children[string[leaf.edgeStart]] = leaf
    return leaf


def breakEdge(node, string, start, offset):
    start_char = string[start]
    mid_char = string[start + offset]
    mid_node = SuffixTreeNode({}, node, node.stringDepth + offset, start, start + offset - 1)
    mid_node.children[mid_char] = node.children[start_char]
    node.children[start_char].parent = mid_node
    mid_node.children[mid_char].edgeStart += offset
    node.children[start_char] = mid_node
    return mid_node


def suffix_array_to_suffix_tree(string, order, lcp_array):
    """
    Build suffix tree of the string text given its suffix array suffix_array
    and LCP array lcp_array. Return the tree as a mapping from a node ID
    to the list of all outgoing edges of the corresponding node. The edges in the
    list must be sorted in the ascending order by the first character of the edge label.
    Root must have node ID = 0, and all other node IDs must be different
    nonnegative integers. Each edge must be represented by a tuple (node, start, end), where
        * node is the node ID of the ending node of the edge
        * start is the starting position (0-based) of the substring of text corresponding to the edge label
        * end is the first position (0-based) after the end of the substring corresponding to the edge label

    For example, if text = "ACACAA$", an edge with label "$" from root to a node with ID 1
    must be represented by a tuple (1, 6, 7). This edge must be present in the list tree[0]
    (corresponding to the root node), and it should be the first edge in the list (because
    it has the smallest first character of all edges outgoing from the root).
    """
    root = SuffixTreeNode({}, None, 0, -1, -1)
    lcp_prev = 0
    curr_node = root
    for i in range(len(string)):
        suffix = order[i]
        while curr_node.stringDepth > lcp_prev:
            curr_node = curr_node.parent
        if curr_node.stringDepth == lcp_prev:
            curr_node = create_new_leaf(curr_node, string, suffix)
        else:
            edge_start = order[i-1] + curr_node.stringDepth
            offset = lcp_prev - curr_node.stringDepth
            mid_node = breakEdge(curr_node, string, edge_start, offset)
            curr_node = create_new_leaf(mid_node, string, suffix)
        if i < len(string) - 1:
            lcp_prev = lcp_array[i]
    return root


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    sa = list(map(int, sys.stdin.readline().strip().split()))
    lcp = list(map(int, sys.stdin.readline().strip().split()))
    print(text)
    # Build the suffix tree and get a mapping from 
    # suffix tree node ID to the list of outgoing Edges.
    tree = suffix_array_to_suffix_tree(text, sa, lcp)
    """
    Output the edges of the suffix tree in the required order.
    Note that we use here the contract that the root of the tree
    will have node ID = 0 and that each vector of outgoing edges
    will be sorted by the first character of the corresponding edge label.
    
    The following code avoids recursion to avoid stack overflow issues.
    It uses two stacks to convert recursive function to a while loop.
    This code is an equivalent of 
    
        OutputEdges(tree, 0);
    
    for the following _recursive_ function OutputEdges:
    
    def OutputEdges(tree, node_id):
        edges = tree[node_id]
        for edge in edges:
            print("%d %d" % (edge[1], edge[2]))
            OutputEdges(tree, edge[0]);
    
    """
    stack = [(tree, 0)]
    result_edges = []
    while len(stack) > 0:
        (node, edge_index) = stack[-1]
        stack.pop()
        if len(node.children) == 0:
            continue
        edges = sorted(node.children.keys())
        if edge_index + 1 < len(edges):
            stack.append((node, edge_index + 1))
        print("%d %d" % (node.children[edges[edge_index]].edgeStart, node.children[edges[edge_index]].edgeEnd + 1))
        stack.append((node.children[edges[edge_index]], 0))
