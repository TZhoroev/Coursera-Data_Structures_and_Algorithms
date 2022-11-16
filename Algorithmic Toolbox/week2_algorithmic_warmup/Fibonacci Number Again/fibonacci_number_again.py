# python3

def fibonacci_number_again_naive(n, m):
    if n <= 1:
        return n
    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m
    return current


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


def fibonacci_number_again(n, m):
    plist = pisa_period(m)
    return plist[n % len(plist)]


if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))
