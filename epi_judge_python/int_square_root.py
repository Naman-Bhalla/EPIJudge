from test_framework import generic_test


def square_root(k):
    left, right = 0, k
    while left < right:
        mid = left + (right - left)//2 
        check = mid ** 2
        if check == k or ((mid + 1) ** 2 > k and check < k):
            return mid
        elif check < k:
            left = mid + 1
        else:
            right = mid - 1
    return left


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_square_root.py",
                                       "int_square_root.tsv", square_root))
