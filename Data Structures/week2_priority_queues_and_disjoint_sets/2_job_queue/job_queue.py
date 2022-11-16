# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["started_at", "worker"])


def assign_jobs(n_workers, jobs):

    def parent(vertex):
        return (vertex-1)//2

    def left_child(vertex):
        return 2*vertex+1

    def right_child(vertex):
        return 2*vertex+2

    def shift_up(H, index):
        while index > 0 and H[parent(index)] > H[index]:
            H[parent(index)], H[index] = H[index], H[parent(index)]
            index = H[parent(index)]
        return H

    def shift_down(h, index):
        min_index = index
        l = left_child(index)
        if l < len(h) and h[l] < h[min_index]:
            min_index = l
        r = right_child(index)
        if r < len(h) and h[r] < h[min_index]:
            min_index = r
        if index != min_index:
            h[index], h[min_index] = h[min_index], h[index]
            shift_down(h, min_index)

    result = []
    next_free_time = [AssignedJob(0, i) for i in range(n_workers)]
    for job in jobs:
        time_finish, worker = next_free_time[0]
        result.append(next_free_time[0])
        next_free_time[0] = AssignedJob(time_finish + job, worker)
        shift_down(next_free_time, 0)
    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
