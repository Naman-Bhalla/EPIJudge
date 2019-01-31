from test_framework import generic_test


def inorder_traversal(tree):
    prev = None
    result = []
    node = tree
    while node:

        if prev == node.parent:
            if node.left:
                next = node.left
            else:
                result.append(node.data)
                next = node.right or node.parent
        elif prev == node.left:
            result.append(node.data)
            next = node.right or node.parent
        else:
            next = node.parent
        prev = node
        node = next
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_with_parent_inorder.py",
                                       'tree_with_parent_inorder.tsv',
                                       inorder_traversal))
