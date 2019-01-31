import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Interval = collections.namedtuple('Interval', ('left', 'right'))

def intervals_sort_method(interval):
    return interval.right

def find_minimum_visits(intervals):
    if not intervals:
        return 0
        
    intervals.sort(key=intervals_sort_method)
    n = len(intervals)
    finish = intervals[0].right
    i = 0
    ans = 0

    while i < n:
        if not intervals[i].left <= finish:
            ans += 1
            finish = intervals[i].right
        i += 1

    return ans + 1


@enable_executor_hook
def find_minimum_visits_wrapper(executor, A):
    A = [Interval(*a) for a in A]
    return executor.run(functools.partial(find_minimum_visits, A))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("minimum_points_covering_intervals.py",
                                       'minimum_points_covering_intervals.tsv',
                                       find_minimum_visits_wrapper))
