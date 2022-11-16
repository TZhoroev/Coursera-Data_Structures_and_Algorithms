# python3
import numpy as np


def lcs3(first_sequence, second_sequence, third_sequence):
    len_first, len_second, len_third = len(first_sequence), len(second_sequence), len(third_sequence)
    d, count = np.zeros((len_first + 1, len_second + 1, len_third + 1)), 0
    d[0, :, :] = np.add.outer(range(len_second + 1), range(len_third + 1))
    d[:, 0, :] = np.add.outer(range(len_first + 1), range(len_third + 1))
    d[:, :, 0] = np.add.outer(range(len_first + 1), range(len_second + 1))
    for k in range(1, len_third + 1):
        for j in range(1, len_second + 1):
            for i in range(1, len_first + 1):
                mdd = d[i, j, k - 1] + 1  # match -deletion- deletion (1-1, 1-3, 2-3)
                dmd = d[i, j - 1, k] + 1  # deletion - match - deletion (1-1, 1-3, 2-3)
                ddm = d[i - 1, j, k] + 1  # deletion - deletion- match (1-1, 1-3, 2-3)
                match = d[i - 1, j - 1, k - 1]  # all- match
                if first_sequence[i - 1] == second_sequence[j - 1] == third_sequence[k - 1]:
                    d[i, j, k] = min(mdd, dmd, ddm, match)
                else: d[i, j, k] = min(mdd, dmd, ddm)
    i, j, k = len_first, len_second, len_third
    while i > 0 or j > 0 or k > 0:
        if i > 0 and d[i, j, k] == d[i - 1, j, k] + 1: i -= 1
        elif j > 0 and d[i, j, k] == d[i, j - 1, k] + 1: j -= 1
        elif k > 0 and d[i, j, k] == d[i, j, k - 1] + 1: k -= 1
        else:
            i -= 1
            j -= 1
            k -= 1
            count += 1
    return count


if __name__ == '__main__':
    n_len = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n_len

    m_len = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m_len

    l_len = int(input())
    c = list(map(int, input().split()))
    assert len(c) == l_len

    print(lcs3(a, b, c))
