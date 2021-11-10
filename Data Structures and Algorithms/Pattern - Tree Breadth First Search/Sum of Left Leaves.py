# Given the root of a binary tree, return the sum of all left leaves.
# Grokking
# Leetcode https://leetcode.com/problems/sum-of-left-leaves/
# Solution https://leetcode.com/problems/sum-of-left-leaves/solution/
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
    result = 0
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
            # add child nodes if they exist
            if current_node.left:
                if not current_node.left.left and not current_node.left.right:
                    result += current_node.left.val
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
    return result


def main():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    result = tree_left_view(root)
    print("Sum of Left leaves: ", result)
    root = TreeNode(3)
    result = tree_left_view(root)
    print("Sum of Left leaves: ", result)


main()
