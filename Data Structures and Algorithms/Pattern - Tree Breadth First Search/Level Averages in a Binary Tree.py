# Given a binary tree, populate an array to represent the averages of all of its levels.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/YQWkA2l67GW
# Leetcode https://leetcode.com/problems/average-of-levels-in-binary-tree/
# Solution https://leetcode.com/problems/average-of-levels-in-binary-tree/solution/
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


def find_level_averages(root):
    result = []
    if not root:
        return result
    queue = deque()
    queue.append(root)
    while queue:
        level_size = len(queue)
        current_level = 0
        for _ in range(level_size):
            # pop left node from queue
            current_node = queue.popleft()
            current_level += current_node.val
            # add child nodes if they exist
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        # add average of current level to result
        result.append(current_level/level_size)
    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level averages are: " + str(find_level_averages(root)))


main()
