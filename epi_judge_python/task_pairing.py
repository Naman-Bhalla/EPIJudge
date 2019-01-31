import collections

from test_framework import generic_test

PairedTasks = collections.namedtuple('PairedTasks', ('task_1', 'task_2'))


def optimum_task_assignment(task_durations):
    n = len(task_durations)
    if n % 2 != 0:
        return -1

    task_durations.sort()
    answer = []
    for i in range(n//2):
        answer.append((task_durations[i], task_durations[n - i - 1]))
    return answer


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("task_pairing.py", 'task_pairing.tsv',
                                       optimum_task_assignment))
