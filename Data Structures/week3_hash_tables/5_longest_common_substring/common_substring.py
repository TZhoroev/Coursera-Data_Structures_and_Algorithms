# python3

import sys
import random
from collections import namedtuple

Answer = namedtuple('answer_type', 'i j len')


def allocate(string, m, multiple):
	s_len = len(string)
	h = [0] * (s_len + 1)
	l_pow = [1] * (s_len + 1)
	for index in range(s_len):
		h[index+1] = (multiple * h[index] + ord(string[index])) % m
		l_pow[index+1] = (multiple * l_pow[index]) % m
	return h, l_pow


def find_substring(hash_table, hash_dict):
	control = False
	matches = {}
	for i in range(len(hash_table)):
		a_start = hash_dict.get(hash_table[i], -1)
		if a_start != -1:
			control = True
			matches[i] = a_start
	return control, matches


def MaxLength(h_s1, h_s2, h_t1, h_t2, l_s1, l_s2, l_t1, l_t2, m1, m2, left, right, l, a, b):
	l = (left + right)//2
	if left > right:
		if l == 0:
			return 0, 0, 0
		return a, b, l
	hash_array1 = {((h_s1[i+l] - l_s1[l] * h_s1[i]) % m1 + m1) % m1: i for i in range(len(h_s1)-l)}
	hash_array2 = [((h_t1[i+l] - l_t1[l] * h_t1[i]) % m1 + m1) % m1 for i in range(len(h_t1)-l)]
	hash_array3 = {((h_s2[i+l] - l_s2[l] * h_s2[i]) % m2 + m2) % m2: i for i in range(len(h_s2)-l)}
	hash_array4 = [((h_t2[i+l] - l_t2[l] * h_t2[i]) % m2 + m2) % m2 for i in range(len(h_t2)-l)]
	check1, matches1 = find_substring(hash_array2, hash_array1)
	check2, matches2 = find_substring(hash_array4, hash_array3)
	if check1 and check2:
		for b, a in matches1.items():
			verify = matches2.get(b, -1)
			if verify == a:
				del hash_array1, hash_array2, hash_array3, hash_array4, matches1, matches2
				return MaxLength(h_s1, h_s2, h_t1, h_t2, l_s1, l_s2, l_t1, l_t2, m1, m2, l + 1, right, l, a, b)
	return MaxLength(h_s1, h_s2, h_t1, h_t2, l_s1, l_s2, l_t1, l_t2, m1, m2, left, l-1, l, a, b)


for line in sys.stdin.readlines():
	s, t = line.split()
	if len(s) == 0 or len(t) == 0:
		print(0, 0, 0)
		break
	m1 = 263130836933693530167218012159999999
	m2 = 8683317618811886495518194401279999999
	multiplier = 513
	h_s1, l_s1 = allocate(s, m1, multiplier)
	h_s2, l_s2 = allocate(s, m2, multiplier)
	h_t1, l_t1 = allocate(t, m1, multiplier)
	h_t2, l_t2 = allocate(t, m2, multiplier)
	s_n, t_n = len(s), len(t)
	left = 0
	right = min(s_n, t_n)
	if s_n <= t_n:
		a, b, l = MaxLength(h_s1, h_s2, h_t1, h_t2, l_s1, l_s2, l_t1, l_t2, m1, m2, left, right, 0, 0, 0)
		print(a, b, l)
	else:
		b, a, l = MaxLength(h_t1, h_t2, h_s1, h_s2, l_t1, l_t2, l_s1, l_s2, m1, m2, left, right, 0, 0, 0)
		print(a, b, l)
