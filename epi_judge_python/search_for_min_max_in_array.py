import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName

MinMax = collections.namedtuple('MinMax', ('smallest', 'largest'))


def find_min_max(A):
    curr_min, curr_max = float('inf'), float('-inf')
    for i in range(0, len(A) - 1, 2):
        if A[i] < A[i + 1]:
            local_min = A[i]
            local_max = A[i + 1]
        else:
            local_min = A[i + 1]
            local_max = A[i]
        curr_min = min(curr_min, local_min)
        curr_max = max(curr_max, local_max)

    if len(A) % 2 != 0:
        curr_min = min(curr_min, A[-1])
        curr_max = max(curr_max, A[-1])
    return MinMax(curr_min, curr_max)


def res_printer(prop, value):
    def fmt(x):
        return 'min: {}, max: {}'.format(x[0], x[1]) if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_for_min_max_in_array.py",
            'search_for_min_max_in_array.tsv',
            find_min_max,
            res_printer=res_printer))
