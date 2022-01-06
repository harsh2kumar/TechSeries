# Given a binary tree, write an iterative algorithm to traverse the tree in-order. Let’s look at the tree below as an example.
# Grokking https://www.educative.io/module/lesson/data-structures-in-python/NEQLzOVynmD
# Leetcode https://leetcode.com/problems/binary-tree-inorder-traversal/
# Solution https://leetcode.com/problems/binary-tree-inorder-traversal/solution/
# Time Complexity The runtime complexity of this solution is linear, O(n).
# Space Complexity The space complexity of this solution is O(h). An iterative solution has O(h) memory complexity as it instantiates a stack
# that has to store information up to the height of the binary tree (h). It will be O(logn) for a balanced tree and, in the worst case, can be O(n).

from BinaryTree import *


def traverse_left_nodes(node, stack):
    while node:
        stack.append(node)
        node = node.left


def inorder_iterative(root):
    result = []
    if root == None:
        return

    stack = deque()
    traverse_left_nodes(root, stack)
    while stack:
        node = stack.pop()
        result.append(str(node.data))
        traverse_left_nodes(node.right, stack)
    return " ".join(result)


arr = [100, 50, 200, 25, 75, 35]
root = create_BST(arr)
print("\nIterative inorder Traversal= ", end="")
print(inorder_iterative(root))
