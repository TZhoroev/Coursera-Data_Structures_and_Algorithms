# python3
import sys
from collections import defaultdict


def InverseBWT(bwt):
    counts = defaultdict(lambda: 0)
    ranks = {}
    for index, letter in enumerate(bwt):
        counts[letter] += 1
        ranks[index] = counts[letter]
    first_letters = {}
    total = 0
    for letter, count in sorted(counts.items()):
        first_letters[letter] = total
        total += count
    word = "$"
    current = 0
    while bwt[current] != "$":
        word += bwt[current]
        current = first_letters[bwt[current]] + ranks[current] - 1
    return word[::-1]


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))

