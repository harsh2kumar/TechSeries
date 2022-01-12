# Given the root node of a binary tree, print the nodes that form the boundary (perimeter).
# Grokking https://www.educative.io/module/lesson/data-structures-in-python/JEv17NxrAZP
# Leetcode https://leetcode.com/problems/boundary-of-binary-tree/
# Solution https://leetcode.com/problems/boundary-of-binary-tree/solution/
# Time Complexity The runtime complexity of this solution is linear, O(n).
# Space Complexity The memory complexity of this solution is O(h). An iterative solution has O(h) memory complexity as it instantiates a stack
# that has to store information up to the height of the binary tree (h). It will be O(logn) for a balanced tree and, in the worst case, can be O(n).

from BinaryTree import *
import sys
import pickle

MARKER = sys.maxsize


def serialize(node, stream):
    # pre-order traversal using DFS
    if not node:
        stream.dump(MARKER)
        return
    stream.dump(node.data)
    serialize(node.left, stream)
    serialize(node.right, stream)


def deserialize(stream):
    # pre-order traversal using DFS
    try:
        data = pickle.load(stream)
        if data == MARKER:
            return None
        node = BinaryTreeNode(data)
        node.left = deserialize(stream)
        node.right = deserialize(stream)
        return node
    except pickle.UnpicklingError:
        return None


arr = [100, 50, 200, 25, 75, 125, 350]
root = create_BST(arr)
display_level_order(root)
output = open('data.class', 'wb')
p = pickle.Pickler(output)
serialize(root, p)
output.close()
input2 = open('data.class', 'rb')
root_deserialized = deserialize(input2)
print("Result:")
display_level_order(root_deserialized)
