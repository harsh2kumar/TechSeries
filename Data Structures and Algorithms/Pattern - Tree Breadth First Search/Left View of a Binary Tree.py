# Given a binary tree, return an array containing nodes in its left view. The left view of a binary tree is the set of nodes visible when the tree is seen
# from the left side.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/gxVWnvZjMn9
# Leetcode
# Solution
# Time Complexity The time complexity of the above algorithm is O(N), where ‘N’ is the total number of nodes in the tree.
# This is due to the fact that we traverse each node once.
# Space Complexity The space complexity of the above algorithm will be O(N) as we need to return a list containing the level order traversal.
# We will also need O(N) space for the queue. Since we can have a maximum of N/2 nodes at any level (this could happen only at the lowest level),
# therefore we will need O(N) space to store them in the queue.

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def tree_left_view(root):
    result = []
    if not root:
        return result
    queue = deque()
    queue.append(root)
    while queue:
        level_size = len(queue)
        left_most_node = -float('inf')
        for _ in range(level_size):
            # pop left node from queue
            current_node = queue.popleft()
            if _ == 0:
                left_most_node = current_node
            # add child nodes if they exist
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        result.append(left_most_node)
    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.left.left.left = TreeNode(3)
    result = tree_left_view(root)
    print("Tree left view: ")
    for node in result:
        print(str(node.val) + " ", end='')


main()
