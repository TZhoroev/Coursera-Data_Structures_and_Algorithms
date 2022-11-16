# python3
import sys


def BWT(context):
    all_rotations = []
    for i in range(len(context)):
        all_rotations.append(context[i:] + context[:i])
    all_rotations.sort()
    result = [word[-1] for word in all_rotations]
    return "".join(result)


if __name__ == '__main__':
    #text = sys.stdin.readline().strip()
    #print(BWT(text))
    print(BWT("AGAAATAGATGATTAGATAGAGGGTAGAATAGATAGATAGATAGATAGGGATGATGATAGATAGATAGATAGATAGAT$"))

