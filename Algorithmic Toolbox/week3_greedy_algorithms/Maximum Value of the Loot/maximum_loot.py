# python3
from sys import stdin
from heapq import heapify, heappop


def maximum_loot_value(capacity, weights, prices, value=0):
    if capacity == 0:
        return value
    unit_prices = [(- p / w, w) for (p, w) in zip(prices, weights)]
    heapify(unit_prices)
    for _ in range(len(prices)):
        max_price, max_weight = heappop(unit_prices)
        max_price = -max_price
        w = min(max_weight, capacity)
        value += w * max_price
        capacity = capacity - w
    return value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    print("{:.10f}".format(opt_value))
