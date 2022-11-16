# python3
import numpy as np


def edit_distance(first_string, second_string):
    n, m = len(first_string), len(second_string)
    d = np.zeros((n+1, m+1))
    d[0, :], d[:, 0] = np.arange(0, m + 1), np.arange(0, n + 1)
    for j in range(1, m+1):
        for i in range(1, n+1):
            insertion, deletion, match, mismatch = d[i, j-1] + 1, d[i-1, j] + 1, d[i-1, j-1], d[i-1, j-1] + 1
            if first_string[i-1] == second_string[j-1]: d[i, j] = min(insertion, deletion, match)
            else: d[i, j] = min(insertion, deletion, mismatch)
    return int(d[-1, -1])


if __name__ == "__main__":
    print(edit_distance(input(), input()))
