# python3
from sys import stdin
import numpy as np


def maximum_gold(capacity, weights):
    n_len = len(weights)
    value = np.zeros((capacity + 1, n_len + 1))
    for i in range(n_len):
        for w in range(1, capacity + 1):
            value[w, i + 1] = value[w, i]
            if weights[i] <= w: value[w, i+1] = max(value[w - weights[i], i] + weights[i], value[w, i + 1])
    return int(value[-1, -1])


if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))
