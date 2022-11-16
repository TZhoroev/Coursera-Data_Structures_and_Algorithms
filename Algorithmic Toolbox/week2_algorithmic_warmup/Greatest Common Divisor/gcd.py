# python3
def gcd_naive(a, b):
    for divisor in range(min(a, b), 0, -1):
        if a % divisor == 0 and b % divisor == 0:
            return divisor
    assert False


def gcd(a, b):
    if b == 0:
        return a
    a, b = b,  a % b
    return gcd(a, b)


if __name__ == '__main__':
    input_a, input_b = map(int, input().split())
    print(gcd(input_a, input_b))
