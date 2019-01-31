from test_framework import generic_test


def is_balanced_binary_tree(tree):
    def helper(tree):
        if not tree:
            return (True, 0)

        is_balanced_left, height_left = helper(tree.left)
        is_balanced_right, height_right = helper(tree.right)

        if (not is_balanced_left) or (not is_balanced_right):
            return (False, max(height_left, height_right))
        return (abs(height_left - height_right) <= 1, max(height_left, height_right) + 1)

    return helper(tree)[0]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_balanced.py",
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
