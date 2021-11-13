# Given a binary tree, find the root-to-leaf path with the maximum sum.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/B815A0y2Ajn
# Leetcode
# Solution
# Time Complexity The time complexity of the above algorithm is O(N^2)
# Space Complexity Tour algorithm’s overall space complexity is O(N*logN).

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxPathSum(root) -> int:
    max_path_sum = []
    current_path_sum = 0
    find_path_sum(root, max_path_sum, current_path_sum)
    return max(max_path_sum)


def find_path_sum(current_node, max_path_sum, current_path_sum):
    if not current_node:
        return
    current_path_sum += current_node.val
    if not current_node.left and not current_node.right:
        max_path_sum.append(current_path_sum)
        # print(max_path_sum)
    # left node
    find_path_sum(current_node.left, max_path_sum, current_path_sum)
    # right node
    find_path_sum(current_node.right, max_path_sum, current_path_sum)
    # backtrack
    current_path_sum -= current_node.val


def main():

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Max Path Sum for Binary Tree : " + str(maxPathSum(root)))


main()
