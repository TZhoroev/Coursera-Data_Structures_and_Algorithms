# python3
import numpy as np


def lcs2(first_sequence, second_sequence):
    n, m = len(first_sequence), len(second_sequence)
    d, count = np.zeros((n+1, m+1)), 0
    d[0, :], d[:, 0] = np.arange(0, m + 1),  np.arange(0, n + 1)
    for j in range(1, m+1):
        for i in range(1, n+1):
            insertion, deletion, match = d[i, j-1] + 1, d[i-1, j] + 1, d[i-1, j-1]
            if first_sequence[i-1] == second_sequence[j-1]: d[i, j] = min(insertion, deletion, match)
            else: d[i, j] = min(insertion, deletion)
    # reverse count
    i, j = n, m
    while i > 0 or j > 0:
        if i > 0 and d[i, j] == d[i-1, j] + 1: i -= 1
        elif j > 0 and d[i, j] == d[i, j-1] + 1: j -= 1
        else:
            i -= 1
            j -= 1
            count += 1
    return count


if __name__ == '__main__':
    n_len = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n_len

    m_len = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m_len

    print(lcs2(a, b))
