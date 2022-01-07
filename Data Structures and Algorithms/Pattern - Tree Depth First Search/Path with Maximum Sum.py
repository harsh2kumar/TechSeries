# Find the path with the maximum sum in a given binary tree. Write a function that returns the maximum sum.
# A path can be defined as a sequence of nodes between any two nodes and doesn’t necessarily pass through the root. The path must contain at least one node.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/xVPgnOvWVJq
# Leetcode https://leetcode.com/problems/binary-tree-maximum-path-sum/
# Solution https://leetcode.com/problems/binary-tree-maximum-path-sum/solution/
# Time Complexity The time complexity of the above algorithm is O(N), where ‘N’ is the total number of nodes in the tree.
# This is due to the fact that we traverse each node once.
# Space Complexity The space complexity of the above algorithm will be O(N) in the worst case. This space will be used to store the recursion stack.
# The worst case will happen when the given tree is a linked list (i.e., every node has only one child).

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class MaximumPathSum:
    def find_maximum_path_sum(self, root):
        self.max_path_sum = -float('inf')
        self.path_sum_recursive(root)
        return self.max_path_sum

    def path_sum_recursive(self, current_node):
        if not current_node:
            return 0

        # ignore paths with negative sums, since we need to find the maximum sum we should
        # ignore any path which has an overall negative sum.
        left_tree_path = max(self.path_sum_recursive(current_node.left), 0)
        right_tree_path = max(self.path_sum_recursive(current_node.right), 0)

        # maximum path sum at the current node will be equal to the sum from the left subtree +
        # the sum from right subtree + val of current node
        local_max_path_sum = left_tree_path+right_tree_path+current_node.val
        # update the global maximum sum
        self.max_path_sum = max(self.max_path_sum, local_max_path_sum)

        # similar to tree diameter
        # maximum sum of any path from the current node will be equal to the maximum of
        # the sums from left or right subtrees plus the value of the current node
        return max(left_tree_path, right_tree_path)+current_node.val


def main():
    maximumPathSum = MaximumPathSum()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    print("Maximum Path Sum: " + str(maximumPathSum.find_maximum_path_sum(root)))
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.right.left = TreeNode(9)
    print("Maximum Path Sum: " + str(maximumPathSum.find_maximum_path_sum(root)))

    root = TreeNode(-1)
    root.left = TreeNode(-3)
    print("Maximum Path Sum: " + str(maximumPathSum.find_maximum_path_sum(root)))


main()
