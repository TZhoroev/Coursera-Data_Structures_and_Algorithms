# python3


def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
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

    def shift_down(h, index, swap=[]):
        max_index = index
        l = left_child(index)
        if l < len(h) and h[l] < h[max_index]:
            max_index = l
        r = right_child(index)
        if r < len(h) and h[r] < h[max_index]:
            max_index = r
        if index != max_index:
            h[index], h[max_index] = h[max_index], h[index]
            swap.append((index, max_index))
            shift_down(h, max_index, swap)
        return h, swap

    def insert(h, p):
        size = len(h)
        h.append(p)
        shift_up(h, size)

    def extract_min(h):
        result = h[0]
        h[0] = h[-1]
        h.pop()
        shift_down(h, 0)
        return result

    swaps = []
    n = len(data)
    for i in range(n//2-1, -1, -1):
        data, swaps = shift_down(data, i, swaps)
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()
