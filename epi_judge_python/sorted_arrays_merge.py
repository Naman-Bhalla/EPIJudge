from test_framework import generic_test
import heapq

def merge_sorted_arrays(sorted_arrays):
    heap = []
    answer = []
    for index, array in enumerate(sorted_arrays):
        heapq.heappush(heap, (array[0], index, 0))

    while heap:
        element, array_idx, inside_idx = heapq.heappop(heap)
        answer.append(element)
        if inside_idx + 1 < len(sorted_arrays[array_idx]):
            heapq.heappush(heap, (sorted_arrays[array_idx][inside_idx + 1], array_idx, inside_idx + 1))
    return answer


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_arrays_merge.py",
                                       "sorted_arrays_merge.tsv",
                                       merge_sorted_arrays))
