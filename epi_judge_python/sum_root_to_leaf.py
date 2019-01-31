from test_framework import generic_test


def sum_root_to_leaf(tree, partial_path_sum=0):
    if not tree:
        return partial_path_sum
    answer = 0
    sum_here = 2 * partial_path_sum
    if tree.data == 1:
        sum_here += 1
    if tree.left:
        answer += sum_root_to_leaf(tree.left, sum_here)
    if tree.right:
        answer += sum_root_to_leaf(tree.right, sum_here)

    if (not tree.left) and (not tree.right):
        return sum_here
        
    return answer


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "sum_root_to_leaf.py", 'sum_root_to_leaf.tsv', sum_root_to_leaf))
