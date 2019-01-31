import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(node0, node1):
    if node0 == node1:
        return node0

    len_1 = 0
    len_0 = 0

    ptr = node1
    while ptr:
        len_1 += 1
        ptr = ptr.parent
    ptr = node0
    while ptr:
        len_0 += 1
        ptr = ptr.parent

    if len_0 > len_1:
        len_1, len_0 = len_0, len_1
        node0, node1 = node1, node0

    diff = len_1 - len_0

    for i in range(diff):
        node1 = node1.parent

    while node1 != node0:
        node1 = node1.parent
        node0 = node0.parent

    return node1


@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0),
                          must_find_node(tree, node1)))

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lowest_common_ancestor_with_parent.py",
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
