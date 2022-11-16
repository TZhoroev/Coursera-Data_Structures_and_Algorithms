# python3

import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
from sys import stdin

import numpy as np

def partition3(values):
    n_len = len(values)
    if sum(values) % 3 != 0: return 0
    sum_1_3 = sum(values)//3
    d_values = np.zeros((n_len + 1, sum_1_3 + 1, sum_1_3 + 1))
    d_values[0, 0, 0], d_values[:, 0, 0] = 1, 1
    for i in range(1, n_len+1):
        for j in range(sum_1_3+1):
            for k in range(sum_1_3+1):
                d_values[i, j, k] = d_values[i - 1, j, k]
                if j >= values[i-1] and d_values[i - 1, j - values[i - 1], k]: d_values[i, j, k] = 1
                if k >= values[i-1] and d_values[i - 1, j, k-values[i-1]]: d_values[i, j, k] = 1
    return 1 if d_values[n_len, sum_1_3, sum_1_3] == 1 else 0


if __name__ == '__main__':

    input_n, *input_values = list(map(int, stdin.read().split()))
    assert input_n == len(input_values)
    print(partition3(input_values))
