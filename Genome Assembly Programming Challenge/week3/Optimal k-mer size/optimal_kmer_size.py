# Uses python3
import sys


def build_kmers(n, reads):
    return [kmer for read in reads for kmer in [read[j:j + n] for j in range(len(read) - n + 1)]]


def whether_opt(n, reads):
    k_mers = set(build_kmers(n, reads))
    prefixes = set()
    suffixes = set()
    for kmer in k_mers:
        prefixes.add(kmer[:-1])
        suffixes.add(kmer[1:])
    return prefixes == suffixes


def Solution():
    reads = sys.stdin.read().strip().split('\n')
    for i in range(len(reads[0]), 1, -1):
        if whether_opt(i, reads):
            print(i)
            break


if __name__ == '__main__':
    Solution()
