from test_framework import generic_test


def get_max_trapped_water(heights):
    n = len(heights)
    l, r = 0, n - 1
    max_area = 0

    while l < r:
        max_area = max(max_area, (r - l) * min(heights[l], heights[r]))

        if heights[l] < heights[r]:
            l += 1
        else:
            r -= 1

    return max_area



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("max_trapped_water.py",
                                       "max_trapped_water.tsv",
                                       get_max_trapped_water))
