# Given the root node of a binary tree, print the nodes that form the boundary (perimeter).
# Grokking https://www.educative.io/module/lesson/data-structures-in-python/JEv17NxrAZP
# Leetcode https://leetcode.com/problems/boundary-of-binary-tree/
# Solution https://leetcode.com/problems/boundary-of-binary-tree/solution/
# Time Complexity The runtime complexity of this solution is linear, O(n).
# Space Complexity The memory complexity of this solution is O(h). An iterative solution has O(h) memory complexity as it instantiates a stack
# that has to store information up to the height of the binary tree (h). It will be O(logn) for a balanced tree and, in the worst case, can be O(n).

from BinaryTree import *


def print_left_perimeter(node, result):
    while node:
        cur_val = node.data
        if node.left:
            node = node.left
        # if left node doesn't exist, we might still want to
        # take the right node as it might be part of left boundary
        elif node.right:
            node = node.right
        else:
            break
        result.append(cur_val)


def print_right_perimeter(node, result):
    stack = []
    while node:
        cur_val = node.data
        if node.right:
            node = node.right
        # if right node doesn't exist, we might still want to
        # take the left node as it might be part of right boundary
        elif node.left:
            node = node.left
        else:
            break
        stack.append(cur_val)
    while stack:
        result.append(stack.pop())


def print_leaves(node, result):
    if not node:
        return
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
        if root.left or root.right:
            print_leaves(root, result)
        print_right_perimeter(root.right, result)
    return result


arr = [100, 50, 200, 25, 60, 350, 10, 70, 400]


root = create_BST(arr)
print("\nPrint tree perimeter\n")
print(display_tree_perimeter(root))
