# python3
from sys import stdin
import pickle


class Equation:
    def __init__(self, a, b):
        self.a = a
        self.b = b


class Position:
    def __init__(self, column, row):
        self.column = column
        self.row = row


def Pivot_Element(a, used_rows, used_columns):
    pivot_element = Position(0, 0)
    while used_rows[pivot_element.row]:
        pivot_element.row += 1
    while used_columns[pivot_element.column]:
        pivot_element.column += 1
    while 0 == a[pivot_element.row][pivot_element.column] or used_rows[pivot_element.row]:
        pivot_element.row += 1
        if pivot_element.row > len(a) - 1:
            return False
    return pivot_element


def SwapLines(a, b, used_rows, pivot_element):
    a[pivot_element.column], a[pivot_element.row] = a[pivot_element.row], a[pivot_element.column]
    b[pivot_element.column], b[pivot_element.row] = b[pivot_element.row], b[pivot_element.column]
    used_rows[pivot_element.column], used_rows[pivot_element.row] = used_rows[pivot_element.row], used_rows[
        pivot_element.column]
    pivot_element.row = pivot_element.column


def ProcessPivotElement(a, rhs, pivot_element):
    size = len(a)
    scale = a[pivot_element.row][pivot_element.column]
    if scale != 1:
        a[pivot_element.row][:] = [item/scale for item in a[pivot_element.row]]
        rhs[pivot_element.row] /= scale
    for index in range(size):
        if index != pivot_element.row:
            scale = a[index][pivot_element.column]
            for j in range(pivot_element.column, size):
                a[index][j] -= a[pivot_element.row][j] * scale
            rhs[index] -= rhs[pivot_element.row] * scale


def MarkPivotElementUsed(pivot_element, used_rows, used_columns):
    used_rows[pivot_element.row] = True
    used_columns[pivot_element.column] = True


def SolveEquation(equation):
    a, rhs = equation.a, equation.b
    size = len(a)
    used_columns, used_rows = [False] * size, [False] * size
    for step in range(size):
        pivot_element = Pivot_Element(a, used_rows, used_columns)
        if not pivot_element:
            return False
        SwapLines(a, rhs, used_rows, pivot_element), ProcessPivotElement(a, rhs, pivot_element)
        MarkPivotElementUsed(pivot_element, used_rows, used_columns)
    return rhs


def checkResult(n, A, b, c, result, last_equation, ans, best_score):
    for r in result:
        if r < -1e-3: return False, ans, best_score
    for index in range(n):
        r = sum([a * num for a, num in zip(A[index], result)])
        if r > b[index] + 1e-3: return False, ans, best_score
    score = sum([cof * num for cof, num in zip(c, result)])
    if score <= best_score: return False, ans, best_score
    else:
        if last_equation: return True, 1, score
        else: return True, 0, score


def solve_diet_problem(n, m, A, b, c, number=1e10):
    for index in range(m):  # add n equation
        e = [0.0] * m
        e[index] = -1.0
        A.append(e), b.append(0.0)
    A.append([1.0] * m), b.append(number)  # add one additional equation
    l = n + m + 1  # total number of equations
    ans = -1
    best_score = -float('inf')
    best_result = None
    for x in range(2 ** l):
        used_index = [index for index in range(l) if ((x / 2 ** index) % 2) // 1 == 1]
        if len(used_index) != m: continue
        last_equation = False
        if used_index[-1] == l - 1: last_equation = True
        As = [A[index] for index in used_index]
        bs = [b[index] for index in used_index]
        result = SolveEquation(pickle.loads(pickle.dumps((Equation(As, bs)))))
        if result:
            increased, ans, best_score = checkResult(
                n, A, b, c, result, last_equation, ans, best_score)
            if increased:
                best_result = result
    return [ans, best_result]


if __name__ == "__main__":
    n, m = list(map(int, stdin.readline().split()))
    A_mat = []
    for i in range(n):
        A_mat += [list(map(int, stdin.readline().split()))]
    b_vec = list(map(int, stdin.readline().split()))
    c_vec = list(map(int, stdin.readline().split()))

    ans_t, ans_x = solve_diet_problem(n, m, A_mat, b_vec, c_vec)

    if ans_t == -1:
        print("No solution")
    if ans_t == 0:
        print("Bounded solution")
        print(' '.join(list(map(lambda x: '%.18f' % x, ans_x))))
    if ans_t == 1:
        print("Infinity")
