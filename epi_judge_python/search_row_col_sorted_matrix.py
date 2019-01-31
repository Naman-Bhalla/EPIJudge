from test_framework import generic_test


def matrix_search(A, x):
    m, n = 0, len(A[0]) - 1

    while m < len(A) and n >=0:
        if A[m][n] < x:
            m += 1
        elif A[m][n] > x:
            n -= 1
        else:
            return True

    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_row_col_sorted_matrix.py",
                                       'search_row_col_sorted_matrix.tsv',
                                       matrix_search))
