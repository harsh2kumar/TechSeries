# Given the root of a binary tree, delete any subtrees whose nodes sum up to zero.
# Grokking https://www.educative.io/module/lesson/data-structures-in-python/g2qjMXrpP0j
# Leetcode
# Solution
# Time Complexity The runtime complexity of this solution is linear, O(n).
# Space Complexity The memory complexity of this solution is O(h). An iterative solution has O(h) memory complexity as it instantiates a stack
# that has to store information up to the height of the binary tree (h). It will be O(logn) for a balanced tree and, in the worst case, can be O(n).

from BinaryTree import *


def delete_zero_sum_subtree_rec(root):
    if not root:
        return 0
    # sum of left subtree
    left_subtree_sum = delete_zero_sum_subtree_rec(root.left)
    # sum of right subtree
    right_subtree_sum = delete_zero_sum_subtree_rec(root.right)
    # if sum is zero, delete that subtree
    if left_subtree_sum == 0:
        root.left = None
    if right_subtree_sum == 0:
        root.right = None
    return (left_subtree_sum + root.data + right_subtree_sum)


def delete_zero_sum_subtree(root):
    if not root:
        return root
    # sum of root, left & right subtrees
    sum_ = delete_zero_sum_subtree_rec(root)
    # if sum is zero, delete tree
    if sum_ == 0:
        root = None
    return root


def create_test_tree1():
    head = BinaryTreeNode(7)
    curr_head = head

    left = BinaryTreeNode(5)
    right = BinaryTreeNode(6)
    curr_head.left = left
    curr_head.right = right

    curr_head = head.left
    left = BinaryTreeNode(-3)
    right = BinaryTreeNode(-2)
    curr_head.left = left
    curr_head.right = right

    return head


root = create_test_tree1()
print("Level Order Traversal:")
display_level_order(root)

delete_zero_sum_subtree(root)
print("Level Order Traversal:")
display_level_order(root)
