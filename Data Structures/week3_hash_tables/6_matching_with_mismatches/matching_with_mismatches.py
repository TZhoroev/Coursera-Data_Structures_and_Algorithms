# python3
import sys
from itertools import islice, tee, repeat


def allocate(string, m, multiple):
	s_len = len(string)
	h = [0] * (s_len + 1)
	l_pow = [1] * (s_len + 1)
	for index in range(s_len):
		h[index+1] = (multiple * h[index] + ord(string[index])) % m
		l_pow[index+1] = (multiple * l_pow[index]) % m
	return h, l_pow


def naive_solver(k, text, pattern):
	position = []
	l_pattern = len(pattern)
	zip_gen = (zip(pattern, islice(text, i, i + l_pattern), repeat(i, l_pattern)) for i in range(len(text) - l_pattern + 1))
	for z in zip_gen:
		l, z = tee(z)
		if sum(1 for i, j, _ in l if i == j) >= l_pattern-k:
			new = zip(*z)
			next(new)
			next(new)
			position.append(next(new)[0])
	return position


def find_substring(text, pattern, hash_text, power_text, hash_pattern, power_pattern, m, index, left, right, mismatch):
	sub_hash1 = ((hash_pattern[right] - power_pattern[right - left] * hash_pattern[left]) % m + m) % m
	sub_hash2 = ((hash_text[index + right] - power_text[right - left] * hash_text[index + left]) % m + m) % m
	if left > right or sub_hash1 == sub_hash2:
		return mismatch
	mid = left + (right - left)//2
	if text[index + mid] != pattern[mid]:
		mismatch += 1
	mismatch1 = find_substring(text, pattern, hash_text, power_text, hash_pattern, power_pattern, m, index, left, mid, mismatch)
	mismatch2 = find_substring(text, pattern, hash_text, power_text, hash_pattern, power_pattern, m, index, mid + 1, right, mismatch)
	mismatch3 = mismatch1 + mismatch2 - mismatch
	return mismatch3


def solve(k, text, pattern):
	m1 = 263130836933693530167218012159999999
	multiple = 513
	indexes = []
	h, l = allocate(text, m1, multiple)
	h_p, l_p = allocate(pattern, m1, multiple)
	p_len = len(pattern)
	for i in range(len(text) - p_len + 1):
		left = 0
		right = p_len
		mismatch = find_substring(text, pattern, h, l, h_p, l_p, m1, i, left, right, 0)
		if mismatch <= k:
			indexes.append(i)
	return indexes


for line in sys.stdin.readlines():
	k, t, p = line.split()
	# ans = naive_solver(int(k), t, p)
	ans = solve(int(k), t, p)
	print(len(ans), *ans)
	#print(len(ans1), *ans1)
