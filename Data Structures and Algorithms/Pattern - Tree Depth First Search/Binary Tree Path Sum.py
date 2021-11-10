# Given a binary tree and a number ‘S’, find if the tree has a path from root-to-leaf such that the sum of all the node values of that path equals ‘S’.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/RMlGwgpoKKY
# Leetcode https://leetcode.com/problems/path-sum/
# Solution https://leetcode.com/problems/path-sum/solution/
# Time Complexity The time complexity of the above algorithm is O(N), where ‘N’ is the total number of nodes in the tree.
# This is due to the fact that we traverse each node once.
# Space Complexity The space complexity of the above algorithm will be O(N) in the worst case. This space will be used to store the recursion stack.
# The worst case will happen when the given tree is a linked list (i.e., every node has only one child).

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def has_path(root, sum):
    # recursive solution
    if not root:
        return False
    # if our node is a leaf node and its value equals sum, we found our valid path
    if root.val == sum and not root.left and not root.right:
        return True
    return has_path(root.left, sum-root.val) or has_path(root.right, sum-root.val)


def main():

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has path: " + str(has_path(root, 23)))
    print("Tree has path: " + str(has_path(root, 16)))


main()
