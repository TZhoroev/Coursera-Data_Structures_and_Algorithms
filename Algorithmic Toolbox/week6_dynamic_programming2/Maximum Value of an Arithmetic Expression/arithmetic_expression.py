# python3
import numpy as np


def min_and_max(i, j,  operation, m, M):
    op = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y}
    minimum, maximum = float('inf'), float('-inf')
    for k in range(i, j):
        a, b = op[operation[k]](M[i, k], M[k+1, j]), op[operation[k]](M[i, k], m[k+1, j])
        c, d = op[operation[k]](m[i, k], M[k+1, j]), op[operation[k]](m[i, k], m[k+1, j])
        minimum, maximum = min(minimum, a, b, c, d), max(maximum, a, b, c, d)
    return minimum, maximum


def find_maximum_value(dataset):
    digits, operation = [], []
    for i in range(len(dataset)):
        if i % 2 == 0: digits.append(int(dataset[i]))
        else: operation.append(dataset[i])
    n_digits = len(digits)
    min_values, max_values = np.zeros((n_digits, n_digits)), np.zeros((n_digits, n_digits))
    np.fill_diagonal(min_values, digits)
    np.fill_diagonal(max_values, digits)
    for s in range(1, n_digits):
        for i in range(n_digits-s):
            j = i + s
            min_values[i, j], max_values[i, j] = min_and_max(i, j, operation, min_values, max_values)
    return int(max_values[0, -1])


if __name__ == "__main__":
    print(find_maximum_value(input()))
