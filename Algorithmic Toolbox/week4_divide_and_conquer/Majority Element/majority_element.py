# python3

def majority_element_naive(elements):
    assert len(elements) <= 10 ** 5
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1
    return 0


def majority_element(elements):
    assert len(elements) <= 10 ** 5
    candidate, votes = float("-inf"), 0
    for i in range(len(elements)):
        if votes == 0:
            candidate, votes = elements[i], 1
        else:
            votes += 1 if elements[i] == candidate else -1
    count = 0
    for i in range(len(elements)):
        if elements[i] == candidate:
            count += 1
    return 1 if count > len(elements) // 2 else 0


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))
