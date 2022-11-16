# python3
import sys


def compute_prefix_function(strings):
    s = [0]*len(strings)
    border = 0
    for i in range(1, len(strings)):
        while (border > 0) and (strings[i] != strings[border]):
            border = s[border - 1]
        if strings[i] == strings[border]:
            border += 1
        else:
            border = 0
        s[i] = border
    return s


def find_pattern(pattern, text):
    """
  Find all the occurrences of the pattern in the text
  and return a list of all positions in the text
  where the pattern starts in the text.
  """
    string = pattern + "$" + text
    s = compute_prefix_function(string)
    result = []
    for i in range(len(pattern) + 1, len(s)):
        if s[i] == len(pattern):
            result.append(i - 2*len(pattern))
    return result


if __name__ == '__main__':
    patterns = sys.stdin.readline().strip()
    texts = sys.stdin.readline().strip()
    result = find_pattern(patterns, texts)
    print(" ".join(map(str, result)))
