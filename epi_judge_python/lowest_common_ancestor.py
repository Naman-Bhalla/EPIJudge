import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(tree, node0, node1):
    def helper(tree, node0, node1x):
        left_count, right_count = 0, 0

        if tree.left:
            left_count, answer = helper(tree.left, node0, node1)
            if left_count >= 2:
                return (2, answer)
        
        if tree.right:
            right_count, answer = helper(tree.right, node0, node1)
            if right_count >= 2:
                return (2, answer)

        total_count = 0
        if tree is node0:
            total_count += 1
        if tree is node1:
            total_count += 1
        total_count += (left_count + right_count)

        if total_count >= 2:
            return (2, tree)
        return (total_count, tree)

    return helper(tree, node0, node1)[1]


@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lowest_common_ancestor.py",
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
