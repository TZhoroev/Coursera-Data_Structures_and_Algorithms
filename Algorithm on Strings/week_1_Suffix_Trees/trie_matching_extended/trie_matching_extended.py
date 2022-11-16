# python3
import sys
from collections import defaultdict


def build_trie(patterns):
	trie = defaultdict(lambda: {})
	reached = defaultdict(lambda: False)
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
		reached[current_node] = True
	return trie, reached


def prefix_trie_matching(subtext, trie, reached):
	subtext = iter(subtext)
	symbol = next(subtext)
	node_v = 0
	while True:
		if reached[node_v]:
			return True
		elif symbol in trie[node_v].keys():
			node_v = trie[node_v][symbol]
			symbol = next(subtext, False)
		else:
			return False


def solve(text, patterns, min_len):
	trie, reached = build_trie(patterns)
	result, k = [], 0
	while k <= len(text) - min_len:
		if prefix_trie_matching(text[k:], trie, reached):
			result.append(k)
		k += 1
	return result


if __name__ == '__main__':
	text = sys.stdin.readline().strip()
	n = int(sys.stdin.readline().strip())
	patterns = []
	min_len = None
	for i in range(n):
		pattern = sys.stdin.readline().strip()
		patterns += [pattern]
		if min_len is None:
			min_len = len(pattern)
		min_len = min(min_len, len(pattern))

	ans = solve(text, patterns, min_len)
	# ans = solve("ATTGTTTTCTCGAGCGC", ["TAATA", "AAGTGAGCAG", "GCTCACATA", "CCAC", "C", "GCC","TGTTCTTA"], 1)
	sys.stdout.write(' '.join(map(str, ans)) + '\n')

