import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def exterior_binary_tree(tree):
    def get_left_boundary(tree, result):
        if tree:
            if tree.left:
                result.append(tree)
                get_left_boundary(tree.left, result)
            elif tree.right:
                result.append(tree)
                get_left_boundary(tree.right, result)

    def get_right_boundary(tree, result):
        if tree:
            if tree.right:
                get_right_boundary(tree.right, result)
                result.append(tree)
            elif tree.left:
                get_right_boundary(tree.left, result)
                result.append(tree)

    def print_leaves_left_to_right(tree, result):
        if tree:
            if (not tree.left) and (not tree.right):
                result.append(tree)
            print_leaves_left_to_right(tree.left, result)
            print_leaves_left_to_right(tree.right, result)
    if not tree:
        return []
    result = [tree]
    get_left_boundary(tree.left, result)
    print_leaves_left_to_right(tree.left, result)
    print_leaves_left_to_right(tree.right, result)
    get_right_boundary(tree.right, result)

    return result


def create_output_list(L):
    if any(l is None for l in L):
        raise TestFailure('Resulting list contains None')
    return [l.data for l in L]


@enable_executor_hook
def create_output_list_wrapper(executor, tree):
    result = executor.run(functools.partial(exterior_binary_tree, tree))

    return create_output_list(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_exterior.py", 'tree_exterior.tsv',
                                       create_output_list_wrapper))
