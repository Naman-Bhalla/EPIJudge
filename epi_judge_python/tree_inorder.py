from test_framework import generic_test


def inorder_traversal(tree):
    if not tree:
        return []
    answer = []
    stack = []

    while stack or tree:
        if tree:
            stack.append(tree)
            tree = tree.left
        else:
            tree = stack.pop()
            answer.append(tree.data)
            tree = tree.right
    return answer


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_inorder.py", 'tree_inorder.tsv',
                                       inorder_traversal))
