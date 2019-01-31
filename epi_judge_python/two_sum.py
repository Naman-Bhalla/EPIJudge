from test_framework import generic_test


def has_two_sum(A, t):
    n = len(A)
    l, r = 0, n - 1
    while l <= r:
        check = A[l] + A[r]
        if check == t:
            return True
        elif check < t:
            l += 1
        else:
            r -= 1
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("two_sum.py", 'two_sum.tsv',
                                       has_two_sum))
