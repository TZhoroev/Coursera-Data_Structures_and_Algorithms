# python3


def last_digit_of_the_sum_of_fibonacci_numbers_again_naive(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    if to_index == 0:
        return 0

    fibonacci_numbers = [0] * (to_index + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, to_index + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers[from_index:to_index + 1]) % 10


def pisa_period(m):
    a = 0
    b = 1
    plist = [a, b]
    for _ in range(1, m*m):
        a, b = b, (a+b) % m
        if (a, b) == (0, 1):
            plist.pop()
            return plist
        plist.append(b)
    plist.pop()
    return plist


def last_digit_of_the_sum_of_fibonacci_numbers_again(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18
    from_index, to_index = from_index % 60, to_index % 60
    plist = [0, 1]
    sum_mn = 0
    for _ in range(from_index-1):
        plist[0], plist[1] = plist[1], (plist[0]+plist[1]) % 10
    for _ in range(from_index, 60):
        sum_mn, plist[0], plist[1] = (sum_mn + plist[1]) % 10, plist[1], (plist[0]+plist[1]) % 10
    plist = [0, 1]
    for _ in range(to_index):
        sum_mn, plist[0], plist[1] = (sum_mn + plist[1]) % 10, plist[1], (plist[0]+plist[1]) % 10
    return sum_mn


if __name__ == '__main__':
    input_from, input_to = map(int, input().split())
    print(last_digit_of_the_sum_of_fibonacci_numbers_again(input_from, input_to))
