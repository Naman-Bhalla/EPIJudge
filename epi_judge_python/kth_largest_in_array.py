from test_framework import generic_test
import random

# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k, A):
    left, right = 0, len(A) - 1
    while left <= right:
        pivot_idx = random.randint(left, right)
        A[pivot_idx], A[right]= A[right], A[pivot_idx]
        pivot = A[right]
        shift_idx = left
        for i in range(left, right):
            if A[i] > pivot:
                A[i], A[shift_idx] = A[shift_idx], A[i]
                shift_idx += 1
        A[shift_idx], A[right] = A[right], A[shift_idx]

        if shift_idx == k - 1:
            return A[shift_idx]
        elif shift_idx > k - 1:
            right = shift_idx - 1
        else:
            left = shift_idx + 1
        
    return A[shift_idx]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("kth_largest_in_array.py",
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
