# Given a binary tree where each node can only have a digit (0-9) value, each root-to-leaf path will represent a number. Find the total sum of all the numbers represented by all paths.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/YQ5o5vEXP69
# Leetcode https://leetcode.com/problems/sum-root-to-leaf-numbers/
# Solution https://leetcode.com/problems/sum-root-to-leaf-numbers/solution/
# Time Complexity The time complexity of the above algorithm is O(N), where ‘N’ is the total number of nodes in the tree.
# This is due to the fact that we traverse each node once.
# Space Complexity The space complexity of the above algorithm will be O(N) in the worst case. This space will be used to store the recursion stack.
# The worst case will happen when the given tree is a linked list (i.e., every node has only one child).

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_sum_of_path_numbers(root) -> int:
    return find_root_to_leaf_node(root, 0)


def find_root_to_leaf_node(current_node, path_sum):
    if not current_node:
        return 0
    path_sum = 10*path_sum+current_node.val
    # if leaf node, return path sum
    if not current_node.left and not current_node.right:
        return path_sum
    return find_root_to_leaf_node(current_node.left, path_sum)+find_root_to_leaf_node(current_node.right, path_sum)


def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


main()
