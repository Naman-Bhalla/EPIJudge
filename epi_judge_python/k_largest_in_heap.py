from test_framework import generic_test, test_utils
import heapq

def k_largest_in_binary_heap(A, k):
    if k <= 1:
        return A[:k]
    answer = []
    heap = [(-A[0], 0)]
    n = len(A)
    if k > n:
        return A

    for i in range(k):
        output, index = heapq.heappop(heap)
        answer.append(-output)
        if 2 * index + 1 < n:
            heapq.heappush(heap, (-A[2 * index + 1], 2 * index + 1))
        if 2 * index + 2 < n:
            heapq.heappush(heap, (-A[2 * index + 2], 2 * index + 2))

    return answer


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "k_largest_in_heap.py",
            "k_largest_in_heap.tsv",
            k_largest_in_binary_heap,
            comparator=test_utils.unordered_compare))
