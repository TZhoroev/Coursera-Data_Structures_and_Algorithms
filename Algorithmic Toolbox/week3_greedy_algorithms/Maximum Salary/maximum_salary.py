# python3

from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))
    largest = 0
    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))
    return largest


def is_better(number, max_number):
    number, max_number = str(number), str(max_number)
    return number+max_number >= max_number+number


def largest_number(numbers):
    if len(numbers) == 0:
        return 0
    your_salary = ""
    while len(numbers) > 0:
        max_number = 0
        for num in numbers:
            if is_better(num, max_number):
                max_number = num
        your_salary += str(max_number)
        numbers.remove(max_number)
    return int(your_salary)


if __name__ == '__main__':
    n = int(input())
    input_numbers = input().split()
    assert len(input_numbers) == n
    print(largest_number(input_numbers))
