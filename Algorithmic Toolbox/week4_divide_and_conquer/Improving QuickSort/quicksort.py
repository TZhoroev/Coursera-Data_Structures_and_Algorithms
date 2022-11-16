# python3

from random import randint


def partition3(array, left, right):
    x, m1, m2 = array[left], left, right
    i = m1
    while i <= m2:
        if array[i] < x:
            array[m1], array[i] = array[i], array[m1]
            m1 += 1
        elif array[i] > x:
            array[m2], array[i] = array[i], array[m2]
            m2 -= 1
            i -= 1
        i += 1
    return m1, m2


def randomized_quick_sort(array, left=0, right=None):
    if left >= right:
        return array
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    m1, m2 = partition3(array, left, right)
    randomized_quick_sort(array, left, m1-1)
    randomized_quick_sort(array, m2+1, right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
