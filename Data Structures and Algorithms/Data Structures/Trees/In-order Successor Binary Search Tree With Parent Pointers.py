# An in-order successor of a node in a binary tree is the next node in an in-order traversal. Write a method to find an in-order successor of a
# given binary tree node in a binary search tree given parent pointers. The following BST has a parent pointer for each node.
# Grokking https://www.educative.io/module/lesson/data-structures-in-python/m2X72YyogJE
# Leetcode https://leetcode.com/problems/inorder-successor-in-bst-ii/
# Solution https://leetcode.com/problems/inorder-successor-in-bst-ii/solution/
# Time Complexity The runtime complexity of this solution is logarithmic, O(logn).
# Space Complexity The space complexity of this solution is constant, O(1).

from BinaryTree import *
from copy import deepcopy


def find_min(root):
    # find the min node/ the left most node
    if not root:
        return None
    while root.left:
        root = root.left
    return root


def find_inorder_successor_bst_parent(node):
    if not node:
        return None
    # if current node has a right child,
    # return the left most node in its right subtree
    if node.right:
        return find_min(node.right)
    # if no right subtree exists, then we need to find the successor
    # in the node's parent
    # go up until we find a node which is the left child of its parent
    # the parent node will be our inorder successor
    while node.parent:
        if node.parent.left == node:
            return node.parent
        node = node.parent
    return None


def find_successor(root, d):
    while root:
        if d > root.data:
            root = root.right
        elif d < root.data:
            root = root.left
        else:
            return find_inorder_successor_bst_parent(root)
    return None


# if we are given just a node in a BST and we know that all nodes have parent links
# we can navigate our way to the inorder successor even if we don't have the root of BST available
def inorder_successor_parent_leetcode(node):
    # if the current node has a right child
    # then its inorder successor will be the right child
    if node.right:
        node = node.right
        while node.left:
            node = node.left
        return node
    # if there isn't a right child
    # then we need to check its parent
    while node.parent:
        if node.parent.left == node:
            return node.parent
        node = node.parent
    return None


arr = [100, 50, 200, 25, 75, 125, 350]
root = create_BST(arr)
populate_parents(root)
all_data = bst_to_list(root)
all_data_copy = deepcopy(all_data)

for d in all_data_copy:
    successor = find_successor(root, d)
    i = all_data.index(d)
    expected_val = None
    if i < len(all_data) - 1:
        expected_val = all_data[i + 1]

    if expected_val != None:
        assert expected_val == successor.data
    else:
        assert successor == None

    if successor:
        print("(" + str(d) + ", " + str(successor.data), end=") ")
    else:
        print("(" + str(d), end=", None)")
