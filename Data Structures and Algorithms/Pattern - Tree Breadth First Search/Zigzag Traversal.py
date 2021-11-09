# Given a binary tree, populate an array to represent its zigzag level order traversal. You should populate the values of all nodes of the first level from left to right,
# then right to left for the next level and keep alternating in the same manner for the following levels.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/qVA27MMYYn0
# Leetcode https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# Solution https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/solution/
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


def traverse(root):
    result = []
    if not root:
        return result
    queue = deque()
    queue.append(root)
    left_to_right = True
    while queue:
        level_size = len(queue)
        current_level = deque()
        for _ in range(level_size):
            # pop left node
            current_node = queue.popleft()
            # add current node to this level
            if left_to_right:
                current_level.append(current_node.val)
            else:
                current_level.appendleft(current_node.val)
            # add child nodes if they exist
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        # add current level to result
        result.append(list(current_level))
        left_to_right = not left_to_right
    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    print("Zigzag traversal: " + str(traverse(root)))


main()
