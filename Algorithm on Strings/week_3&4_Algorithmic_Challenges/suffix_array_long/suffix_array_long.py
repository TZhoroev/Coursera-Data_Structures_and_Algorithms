# python3
import sys
from collections import defaultdict


def sort_characters(string):
    order = [0]*len(string)
    count = defaultdict(lambda: 0)
    for i in range(len(string)):
        count[string[i]] += 1
    keys = sorted(count.keys())
    prev_key = keys[0]
    for key in keys[1:]:
        count[key] += count[prev_key]
        prev_key = key
    for i in range(len(string) - 1, -1, -1):
        c = string[i]
        count[c] += -1
        order[count[c]] = i
    return order


def compute_char_classes(string, order):
    char_class = [0]*len(string)
    char_class[order[0]] = 0
    for i in range(1, len(string)):
        if string[order[i]] != string[order[i - 1]]:
            char_class[order[i]] = char_class[order[i - 1]] + 1
        else:
            char_class[order[i]] = char_class[order[i - 1]]
    return char_class


def sort_doubled(string, length, order, char_class):
    n = len(string)
    count = [0] * n
    new_order = [0] * n
    for i in range(n):
        count[char_class[i]] += 1
    for j in range(1, n):
        count[j] += count[j-1]
    for i in range(n - 1, -1, -1):
        start = (order[i] - length + n) % n
        c = char_class[start]
        count[c] += -1
        new_order[count[c]] = start
    return new_order


def update_classes(new_order, char_class, length):
    n = len(new_order)
    new_class = [0] * n
    new_class[new_order[0]] =0
    for i in range(1, n):
        cur, prev = new_order[i], new_order[i-1]
        mid, mid_prev = cur + length, (prev + length) % n
        if char_class[cur] != char_class[prev] or char_class[mid] != char_class[mid_prev]:
            new_class[cur] = new_class[prev] + 1
        else:
            new_class[cur] = new_class[prev]
    return new_class


def build_suffix_array(string):
    """
  Build suffix array of the string text and
  return a list result of the same length as the text
  such that the value result[i] is the index (0-based)
  in text where the i-th lexicographically smallest
  suffix of text starts.
  """
    order = sort_characters(string)
    char_class = compute_char_classes(string, order)
    length = 1
    while length < len(string):
        order = sort_doubled(string, length, order, char_class)
        char_class = update_classes(order, char_class, length)
        length *= 2
    return order


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(" ".join(map(str, build_suffix_array(text))))
