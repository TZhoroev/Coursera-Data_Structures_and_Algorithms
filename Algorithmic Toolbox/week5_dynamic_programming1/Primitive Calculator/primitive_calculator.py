# python3
def compute_operations(n):
    all_parents = [None] * (n + 1)
    all_min_ops = [0] + [None] * n
    for k in range(1, n + 1):
        curr_parent = k - 1
        curr_min_ops = all_min_ops[curr_parent] + 1
        if k % 3 == 0:
            parent = k // 3
            num_ops = all_min_ops[parent] + 1
            if num_ops < curr_min_ops: curr_parent, curr_min_ops = parent, num_ops
        elif k % 2 == 0:
            parent = k // 2
            num_ops = all_min_ops[parent] + 1
            if num_ops < curr_min_ops: curr_parent, curr_min_ops = parent, num_ops
        all_parents[k], all_min_ops[k] = curr_parent, curr_min_ops
    numbers, k = [], n
    while k > 0:
        numbers.append(k)
        k = all_parents[k]
    numbers.reverse()
    return numbers


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
