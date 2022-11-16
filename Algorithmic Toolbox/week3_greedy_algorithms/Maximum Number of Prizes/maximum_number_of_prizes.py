# python3


def compute_optimal_summa(n):
    assert 1 <= n <= 10 ** 9
    summa = []
    i = 0
    n_copy = n
    while n - i > 0:
        i = i + 1
        n = n - i
        summa.append(i)
    k = n_copy - sum(summa)
    summa[-1] += k
    return summa


if __name__ == '__main__':
    input_n = int(input())
    output_summa = compute_optimal_summa(input_n)
    print(len(output_summa))
    print(*output_summa)
