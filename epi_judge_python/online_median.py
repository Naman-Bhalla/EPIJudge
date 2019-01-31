from test_framework import generic_test
import heapq

def online_median(sequence):
    max_heap, min_heap = [], []
    result = []
    for item in sequence:
        heapq.heappush(max_heap, -heapq.heappushpop(min_heap, item))
        if len(max_heap) > len(min_heap):
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
            result.append(min_heap[0])
        else:
            result.append((-max_heap[0] + min_heap[0]) / 2)
    return result


def online_median_wrapper(sequence):
    return online_median(iter(sequence))

# 1 -----> 2

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("online_median.py", "online_median.tsv",
                                       online_median_wrapper))
