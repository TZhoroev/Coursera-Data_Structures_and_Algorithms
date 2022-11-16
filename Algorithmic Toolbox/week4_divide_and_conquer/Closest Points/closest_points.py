# python3
from collections import namedtuple
from itertools import combinations
from math import sqrt

Point = namedtuple('Point', 'x y')


def distance_squared(first_point, second_point):
    return (first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2


def minimum_distance_squared_naive(points):
    min_distance_squared = float("inf")
    for p, q in combinations(points, 2):
        min_distance_squared = min(min_distance_squared, distance_squared(p, q))
    return min_distance_squared


def strip_closest(strip, size, d):
    min_val = d
    for i in range(size):
        j = i + 1
        while j < size and j < i + 9:
            min_val = min(distance_squared(strip[i], strip[j]), min_val)
            j += 1
    return min_val


def closest_util(points):
    n_points = len(points)
    if n_points == 1:
        return float("inf")
    elif n_points == 2:
        return distance_squared(points[0], points[1])
    elif n_points == 3:
        return min(distance_squared(points[0], points[1]), distance_squared(points[1], points[2]), distance_squared(points[0], points[2]))
    mid = (n_points + 1) // 2
    left_points, mid_point, right_points = points[:mid], points[mid], points[mid:]  # partition of array

    min_dist = min(closest_util(left_points), closest_util(right_points))  # take minimum distance of two partition

    strip_p = [point for point in points if abs(point.x - mid_point.x) < min_dist]  # find all points around mid_point with distance small enough
    strip_p.sort(key=lambda point: point.y)  # short them in terms of y

    return min(min_dist, strip_closest(strip_p, len(strip_p), min_dist))


def minimum_distance_squared(points):
    points.sort(key=lambda point: point.x)
    return closest_util(points)


if __name__ == '__main__':
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)

    print("{0:.9f}".format(sqrt(minimum_distance_squared(input_points))))
