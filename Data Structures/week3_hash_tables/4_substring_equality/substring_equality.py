# python3
import sys
import random


class Solver:
	def __init__(self, string):
		self.s = string
		self.n = len(string)

	def allocate(self, m, multiplier):
		h = [0] * (self.n + 1)
		l = [1] *(self.n + 1)
		for index in range(self.n):
			h[index+1] = (multiplier * h[index] + ord(self.s[index])) % m
			l[index+1] = (multiplier * l[index]) % m
		return h, l


s = sys.stdin.readline()
q = int(sys.stdin.readline())
m1 = pow(10, 9) + 7
m2 = pow(10, 9) + 9
multiplier = random.randint(0, pow(10, 9))
solver = Solver(s)
h1, l1 = solver.allocate(m1, multiplier)
h2, l2 = solver.allocate(m2, multiplier)
for i in range(q):
	a, b, l = map(int, sys.stdin.readline().split())
	result1 = (h1[a+l] - h1[b+l] - l1[l]*(h1[a] - h1[b])) % m1 == 0
	result2 = (h2[a+l] - h2[b+l] - l2[l]*(h2[a] - h2[b])) % m2 == 0
	print("Yes" if result1 and result2 else "No")
