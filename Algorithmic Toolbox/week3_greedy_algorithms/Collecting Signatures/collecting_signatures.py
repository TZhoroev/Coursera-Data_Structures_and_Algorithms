# python3

from collections import namedtuple
from sys import stdin

Segment = namedtuple('Segment', 'start end')


def compute_optimal_points(segments):
    segments.sort(key=lambda x: x[1])
    coordinates = []
    i = 0
    len_segment = len(segments)
    while i < len_segment:
        seg = segments[i][1]
        coordinates.append(seg)
        p = i + 1
        if p >= len_segment:
            break
        arrived = segments[p][0]
        while seg >= arrived:
            p += 1
            if p >= len_segment:
                break
            arrived = segments[p][0]
        i = p
    return coordinates


if __name__ == '__main__':
    n, *data = map(int, stdin.read().split())
    input_segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    assert n == len(input_segments)
    output_points = compute_optimal_points(input_segments)
    print(len(output_points))
    print(*output_points)
