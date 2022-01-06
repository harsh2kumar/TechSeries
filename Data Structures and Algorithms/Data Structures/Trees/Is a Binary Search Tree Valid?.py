# Given a Binary Tree, figure out whether it’s a Binary Search Tree. In a binary search tree, each node’s key value is smaller than the key
# value of all nodes in the right subtree, and are greater than the key values of all nodes in the left subtree i.e. L < N < R.
# Grokking https://www.educative.io/module/lesson/data-structures-in-python/m2X72YyogJE
# Leetcode https://leetcode.com/problems/validate-binary-search-tree/
# Solution https://leetcode.com/problems/validate-binary-search-tree/solution/
# Time Complexity The runtime complexity of this solution is linear, O(n).
# Space Complexity The memory complexity of this solution is linear, O(n).

from BinaryTree import *


def is_valid_bst(root, low, high):
    # if the current node is a leaf node
    # return True
    if not root:
        return True
    val = root.data
    return (val > low and val < high) and (is_valid_bst(root.left, low, val)) and (is_valid_bst(root.right, val, high))


def is_bst(root):
    return is_valid_bst(root, float('-inf'), float('inf'))


root = BinaryTreeNode(100)
insert(root, 50)
insert(root, 200)
insert(root, 25)
# Add a node at an incorrect position
# insert_inorder_binary_tree(root, 125)
insert(root, 150)
insert(root, 350)
display_inorder(root)
# Add a node at an incorrect position
if is_bst(root) == True:
    print("\nTrue")
else:
    print("\nFalse")
root = BinaryTreeNode(12)
root.left = BinaryTreeNode(7)
root.right = BinaryTreeNode(1)
root.left.left = BinaryTreeNode(9)
root.right.left = BinaryTreeNode(10)
root.right.right = BinaryTreeNode(5)
display_inorder(root)

if is_bst(root) == True:
    print("\nTrue")
else:
    print("\nFalse")
