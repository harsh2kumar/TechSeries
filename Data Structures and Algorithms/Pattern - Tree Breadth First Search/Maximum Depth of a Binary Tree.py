# FGiven a binary tree, find its maximum depth (or height).
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/3jwVx84OMkO
# Leetcode https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Solution https://leetcode.com/problems/maximum-depth-of-binary-tree/solution/
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


def find_minimum_depth(root):
    max_tree_depth = 0
    if not root:
        return max_tree_depth
    queue = deque()
    queue.append(root)
    while queue:
        max_tree_depth += 1
        level_size = len(queue)
        for _ in range(level_size):
            # pop left node from queue
            current_node = queue.popleft()
            # add child nodes if they exist
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
    return max_tree_depth


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))


main()
