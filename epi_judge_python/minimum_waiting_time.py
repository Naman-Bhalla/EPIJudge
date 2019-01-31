from test_framework import generic_test


def minimum_total_waiting_time(service_times):
    service_times.sort()
    n = len(service_times)
    curr_sum = 0
    for i in range(n - 1):
        curr_sum += service_times[i] * (n - i - 1)

    return curr_sum


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("minimum_waiting_time.py",
                                       'minimum_waiting_time.tsv',
                                       minimum_total_waiting_time))
