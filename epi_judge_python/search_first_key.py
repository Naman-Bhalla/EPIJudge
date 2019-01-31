from test_framework import generic_test


def search_first_of_k(A, k):
    n = len(A)
    left, right = 0, n - 1

    while left <= right:
        mid = left + (right - left)//2

        if A[mid] == k and (mid == 0 or A[mid - 1] != k):
            return mid
        elif A[mid] < k:
            left = mid + 1
        elif A[mid] >= k:
            right = mid - 1

    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_first_key.py", 'search_first_key.tsv', search_first_of_k))
