from test_framework import generic_test


def calculate_largest_rectangle(heights):
    stack = []
    max_area = 0

    for index, height in enumerate(heights + [0]):
        while stack and heights[stack[-1]] >= height:
            idx = stack.pop()
            width = index if not stack else index - stack[-1] - 1
            h = heights[idx]

            max_area = max(max_area, width * h)

        stack.append(index)

    return max_area


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("largest_rectangle_under_skyline.py",
                                       'largest_rectangle_under_skyline.tsv',
                                       calculate_largest_rectangle))
