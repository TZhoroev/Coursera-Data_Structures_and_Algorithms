# python3

from collections import namedtuple
from collections import deque

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


def process_packets(packets, buffer_size):
    buffe = deque(maxlen=buffer_size)

    start_times = [None] * len(packets)
    for i, (arrival, duration) in enumerate(packets):
        while buffe and buffe[0] <= arrival:
            buffe.popleft()

        if len(buffe) >= buffer_size:
            start_times[i] = -1
        else:
            start_times[i] = max(arrival, buffe[-1] if buffe else 0)
            buffe.append(start_times[i] + duration)
    return start_times


if __name__ == "__main__":
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))
    out = process_packets(requests, buffer_size)
    for item in out:
        print(item)
