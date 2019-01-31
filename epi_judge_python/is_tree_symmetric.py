from test_framework import generic_test


def is_symmetric(tree):
    def helper(left, right):
        if (not left) and (not right):
            return True
        if (left and (not right)) or (right and (not left)):
            return False
        if left.data == right.data:
            return helper(left.left, right.right) and helper(left.right, right.left)
        return False
    if not tree:
        return True
    return helper(tree.left, tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_symmetric.py",
                                       'is_tree_symmetric.tsv', is_symmetric))
