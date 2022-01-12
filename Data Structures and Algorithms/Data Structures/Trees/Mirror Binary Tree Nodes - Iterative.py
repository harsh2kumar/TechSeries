# Given the root node of a binary tree, swap the ‘left’ and ‘right’ children for each node.
# Grokking https://www.educative.io/module/lesson/data-structures-in-python/7DkL5MJZ918
# Leetcode https://leetcode.com/problems/invert-binary-tree/
# Solution https://leetcode.com/problems/invert-binary-tree/solution/
# Time Complexity The runtime complexity of this solution is linear, O(n).
# Space Complexity The memory complexity of this solution is O(h). An iterative solution has O(h) memory complexity as it instantiates a stack
# that has to store information up to the height of the binary tree (h). It will be O(logn) for a balanced tree and, in the worst case, can be O(n).

from BinaryTree import *
from collections import deque


def mirror_tree(root):
    if root == None:
        return
    queue = deque()
    queue.append(root)
    while queue:
        node = queue.popleft()
        tmp = node.left
        node.left = node.right
        node.right = tmp
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return root


arr = [20, 50, 200, 75, 25, 300]
root = create_BST(arr)

display_level_order(root)
mirror_tree(root)
print("\nMirrored Level Order Traversal:")
display_level_order(root)
