# python3
from sys import stdin


def Solution(A, b, n_var):
    clauses = []
    for index, coefficient in enumerate(A):
        non_0_coefficient = [(j, coefficient[j]) for j in range(m) if coefficient[j] != 0]
        l = len(non_0_coefficient)
        for x in range(2**l):
            curr_set = [non_0_coefficient[j] for j in range(l) if ((x/2 ** j) % 2)//1 == 1]
            curr_sum = sum([factor[1] for factor in curr_set])
            if curr_sum > b[index]:
                clauses.append([-(factor[0]+1) for factor in curr_set] + [factor[0]+1 for factor in non_0_coefficient if factor not in curr_set])
    if 0 == len(clauses):
        clauses.append([1, -1])
        n_var = 1
    return n_var, clauses


if __name__ == '__main__':
    n, m = list(map(int, stdin.readline().split()))
    A_mat = []
    for i in range(n):
        A_mat += [list(map(int, stdin.readline().split()))]
    b_vec = list(map(int, stdin.readline().split()))
    m, clause = Solution(A_mat, b_vec, m)
    print(len(clause), m)
    for c in clause:
        c.append(0)
        print(' '.join(map(str, c)))
