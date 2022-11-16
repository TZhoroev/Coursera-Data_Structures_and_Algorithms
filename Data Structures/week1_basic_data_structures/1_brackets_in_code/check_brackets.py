# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    opening_index = []
    for i, char in enumerate(text):
        if char in "([{":
            opening_brackets_stack.append(char)
            opening_index.append(i+1)
        if char in ")]}":
            if len(opening_brackets_stack) == 0:
                return i+1
            last = opening_brackets_stack.pop()
            opening_index.pop()
            if not are_matching(last, char):
                return i+1
    if len(opening_index) != 0:
        return opening_index[-1]
    else:
        return "Success"


def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()
