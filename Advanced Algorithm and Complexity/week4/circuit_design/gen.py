import pycosat
import itertools
import random

pos = list(range(-50, 0))  # adjust range for smaller test cases
neg = list(range(1, 51))  # adjust range for smaller test cases
tot = pos + neg

c = list(itertools.combinations(tot, 2))


def make_test(tot):
        c = list(itertools.combinations(tot, 2))
        tests = random.choices(c, k=150)  # adjust k for smaller test cases
        cnf = [list(test) for test in tests]
        if pycosat.solve(cnf) != "UNSAT":
            for element in cnf:
                print(element[0], element[1])
            for sol in pycosat.itersolve(cnf):
                print("SATISFIABLE")
                print(" ".join(map(str, sol)))
        else:
            for element in cnf:
                print(element[0], element[1])
            print("UNSATISFIABLE")

    # if pycosat.solve(cnf) != "SAT":
    #     return tests, cnf


make_test(tot)

# tests, cnf = make_test(tot)
# print(tests)
# print(cnf)
