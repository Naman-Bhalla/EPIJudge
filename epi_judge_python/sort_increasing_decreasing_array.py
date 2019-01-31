from test_framework import generic_test
import sorted_arrays_merge

def sort_k_increasing_decreasing_array(A):
    INCREASING, DECREASING = 0, 1
    n = len(A)
    inc = INCREASING
    sorted_arrays = []
    start = 0
    for i in range(1, n + 1):
        if (i == n) or (A[i] > A[i - 1] and inc == DECREASING) or (A[i] < A[i - 1] and inc == INCREASING):
            if inc == DECREASING:
                sorted_arrays.append(A[i - 1:start - 1:-1])
            else:
                sorted_arrays.append(A[start:i])
            inc = DECREASING
            start = i
    return sorted_arrays_merge.merge_sorted_arrays(sorted_arrays)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sort_increasing_decreasing_array.py",
                                       'sort_increasing_decreasing_array.tsv',
                                       sort_k_increasing_decreasing_array))
