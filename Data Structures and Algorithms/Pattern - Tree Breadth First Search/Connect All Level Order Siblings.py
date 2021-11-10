# Given a binary tree, connect each node with its level order successor. The last node of each level should point to the first node of the next level.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/qVxy1qop77p
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
        self.left, self.right, self.next = None, None, None

    # tree traversal using 'next' pointer
    def print_tree(self):
        print("Traversal using 'next' pointer: ", end='')
        current = self
        while current:
            print(str(current.val) + " ", end='')
            current = current.next


def connect_all_siblings(root):
    if not root:
        return None
    queue = deque()
    queue.append(root)
    prev_node = None
    while queue:
        # pop left node from queue
        current_node = queue.popleft()
        if prev_node:
            prev_node.next = current_node
        prev_node = current_node
        # add child nodes if they exist
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
    return root


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    connect_all_siblings(root)
    root.print_tree()


main()
