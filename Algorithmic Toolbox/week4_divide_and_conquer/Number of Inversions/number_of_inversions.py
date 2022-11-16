# python3

from itertools import combinations


def compute_inversions_naive(a):
    number_of_inversions = 0
    for i, j in combinations(range(len(a)), 2):
        if a[i] > a[j]:
            number_of_inversions += 1
    return number_of_inversions


def merge(left, right, count):
    r, l = len(right), len(left)
    d = [0] * (r + l)
    i = j = k = 0
    while i < r and j < l:
        if left[j] <= right[i]:
            d[k] = left[j]
            j += 1
        else:
            d[k] = right[i]
            count += (l - j)
            i += 1
        k += 1
    while j < len(left):
        d[k] = left[j]
        j += 1
        k += 1

    while i < len(right):
        d[k] = right[i]
        i += 1
        k += 1
    return d, count


def mergesort(a, count=0):
    n = len(a)
    if n == 1:
        return a, count
    m = n // 2
    b, c = a[:m], a[m:]
    (b, count1) = mergesort(b, count)
    (c, count2) = mergesort(c, count)
    count = count1 + count2
    a, count = merge(b, c, count)
    return a, count


def compute_inversions(a):
    a, count = mergesort(a)
    return count


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(compute_inversions(elements))
