from test_framework import generic_test
import heapq

def sort_approximately_sorted_array(sequence, k):
    heap = []
    result = []
    out = 0
    for _ in range(k):
        num = next(sequence, None)
        if num is not None:
            heapq.heappush(heap, num)
        else:
            break
    while heap:
        num = next(sequence, None)
        if num is not None:
            result.append(heapq.heappushpop(heap, num))

        else:
            break

    while heap:
        result.append(heapq.heappop(heap))
    return result


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "sort_almost_sorted_array.py", 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
