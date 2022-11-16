# python3
import random


def read_input():
    return input().rstrip(), input().rstrip()


def print_occurrences(output):
    print(' '.join(map(str, output)))


def poly_hash(string, prime, multiplier):
    ans = 0
    for s in reversed(string):
        ans = (ans*multiplier + ord(s)) % prime
    return ans


def pre_compute_hashes(text, pattern_size, prime, multiplier):
    h = [0]*(len(text)-pattern_size+1)
    s = text[len(text)-pattern_size:]
    h[-1] = poly_hash(s, prime, multiplier)
    y = 1
    for i in range(1, pattern_size+1):
        y = y * multiplier % prime
    for i in range(len(text)-pattern_size-1, -1, -1):
        h[i] = (h[i+1]*multiplier + ord(text[i]) - y * ord(text[i + pattern_size])) % prime
    return h


def get_occurrences(pattern, text):
    prime = 2147483659
    multiplier = random.randint(0, prime-1)
    result = []
    pattern_size = len(pattern)
    p_hash = poly_hash(pattern, prime, multiplier)
    h = pre_compute_hashes(text, pattern_size, prime, multiplier)
    for i in range(len(text)-pattern_size+1):
        if p_hash != h[i]:
            continue
        elif text[i:i+pattern_size] == pattern:
            result.append(i)
    return result


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

