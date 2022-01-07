# Given the root node of a binary tree, print the nodes that form the boundary (perimeter).
# Grokking https://www.educative.io/module/lesson/data-structures-in-python/JEv17NxrAZP
# Leetcode https://leetcode.com/problems/boundary-of-binary-tree/
# Solution https://leetcode.com/problems/boundary-of-binary-tree/solution/
# Time Complexity The runtime complexity of this solution is linear, O(n).
# Space Complexity The memory complexity of this solution is O(h). An iterative solution has O(h) memory complexity as it instantiates a stack
# that has to store information up to the height of the binary tree (h). It will be O(logn) for a balanced tree and, in the worst case, can be O(n).

from BinaryTree import *


def print_left_perimeter(node, result):
    if node:
        if node.left:
            result.append(node.data)
            print_left_perimeter(node.left, result)
        # if left node doesn't exist, we might still want to
        # take the right node as it might be part of left boundary
        elif node.right:
            print_left_perimeter(node.right, result)
            result.append(node.data)


def print_right_perimeter(node, result):
    # since recursion calls already use a stack,
    # the order of results will be bottom-up if we append
    # into result array after the call to print_right_perimeter
    if node.right:
        print_right_perimeter(node.right, result)
        result.append(node.data)
    # if right node doesn't exist, we might still want to
    # take the left node as it might be part of right boundary
    elif node.left:
        print_right_perimeter(node.left, result)
        result.append(node.data)


def print_leaves(node, result):
    if node:
        # perform in-order traversal
        print_leaves(node.left, result)
        # add to leaf nodes to result
        if not node.left and not node.right:
            result.append(node.data)
        print_leaves(node.right, result)


def display_tree_perimeter(root):
    result = []
    if root:
        result.append(root.data)
        print_left_perimeter(root.left, result)
        # print the leaves if either/ both left subtree or/and right subtree
        # print all leaf nodes
        print_leaves(root.left, result)
        print_leaves(root.right, result)
        print_right_perimeter(root.right, result)
    return result


arr = [100, 50, 200, 25, 60, 350, 10, 70, 400]


root = create_BST(arr)
print("\nPrint tree perimeter\n")
print(display_tree_perimeter(root))
