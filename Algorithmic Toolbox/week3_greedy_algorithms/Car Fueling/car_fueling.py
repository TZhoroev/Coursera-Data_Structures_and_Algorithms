# python3

def compute_min_number_of_refills(d, m, stops):
    n = len(stops)
    stops.insert(0, 0)
    stops.append(d)
    num_refill = current_fill = 0
    while current_fill <= n:
        last_fill = current_fill
        while current_fill <= n and stops[(current_fill + 1)] - stops[last_fill] <= m:
            current_fill += 1
        if current_fill == last_fill:
            return -1
        if current_fill <= n:
            num_refill += 1
    return num_refill


if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))
