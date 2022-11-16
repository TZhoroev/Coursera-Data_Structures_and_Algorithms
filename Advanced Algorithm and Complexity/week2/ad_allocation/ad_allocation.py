# python3
from sys import stdin
import numpy as np
from scipy.optimize import linprog


def allocate_ads(A, b, c):
    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))
    return res


n, m = list(map(int, stdin.readline().split()))
A = []
for i in range(n):
    A += [list(map(int, stdin.readline().split()))]
b = list(map(int, stdin.readline().split()))
c = list(map(int, stdin.readline().split()))
A = np.array(A)
b = np.array(b)
c = np.array(c)
result = allocate_ads(A, b, -c)

if result.status == 2:
    print("No solution")
if result.status == 0:
    print("Bounded solution")
    print(' '.join(list(map(lambda x: '%.18f' % x, result.x))))
if result.status == 3:
    print("Infinity")
