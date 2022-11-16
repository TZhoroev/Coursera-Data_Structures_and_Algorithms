# python3
import sys


def solve(p, q):
    l = len(p)
    m = len(q)
    for i in range(min(l, m)):
        for j in range(l - i):
            s = p[j:j + i + 1]
            if s not in q:
                return s
    return


p = sys.stdin.readline().strip()
q = sys.stdin.readline().strip()

ans = solve(p, q)

sys.stdout.write(ans + '\n')
