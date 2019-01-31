from test_framework import generic_test
from binary_tree_node import BinaryTreeNode


def binary_tree_from_preorder_inorder(preorder, inorder):
    inorder_indices = {data: index for index, data in enumerate(inorder)}
    def helper(preorder_start, preorder_end, inorder_start, inorder_end):
        if preorder_end <= preorder_start or inorder_end <= inorder_start:
            return None
        pivot = preorder[preorder_start]
        index_in = inorder_indices[pivot]
        size = index_in - inorder_start
        return BinaryTreeNode(
                        pivot, 
                        helper(preorder_start + 1, preorder_start + size + 1, inorder_start, index_in),
                        helper(preorder_start + size + 1, preorder_end, index_in + 1, inorder_end)
        )
    return helper(0, len(preorder), 0, len(inorder))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_from_preorder_inorder.py",
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
