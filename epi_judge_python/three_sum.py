from test_framework import generic_test
import two_sum

def has_three_sum(A, t):
    A.sort()
    return any(two_sum.has_two_sum(A, t - a) for a in A)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("three_sum.py", "three_sum.tsv",
                                       has_three_sum))
