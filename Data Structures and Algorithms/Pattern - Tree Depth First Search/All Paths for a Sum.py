# Given a binary tree and a number ‘S’, find all paths from root-to-leaf such that the sum of all the node values of each path equals ‘S’.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/B815A0y2Ajn
# Leetcode https://leetcode.com/problems/path-sum-ii/
# Solution https://leetcode.com/problems/path-sum-ii/solution/
# Time Complexity The time complexity of the above algorithm is O(N^2)
# Space Complexity Tour algorithm’s overall space complexity is O(N*logN).

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_paths(root, required_sum):
    all_paths = []
    find_paths_recursive(root, required_sum, [], all_paths)
    return all_paths


def find_paths_recursive(current_node, required_sum, current_path, all_paths):
    if current_node is None:
        return

    # add the current node to the path
    current_path.append(current_node.val)

    # if the current node is a leaf and its value is equal to required_sum, save the current path
    if current_node.val == required_sum and current_node.left is None and current_node.right is None:
        all_paths.append(list(current_path))
    else:
        # traverse the left sub-tree
        find_paths_recursive(current_node.left, required_sum -
                             current_node.val, current_path, all_paths)
        # traverse the right sub-tree
        find_paths_recursive(current_node.right, required_sum -
                             current_node.val, current_path, all_paths)

    # remove the current node from the path to backtrack,
    # we need to remove the current node while we are going up the recursive call stack.
    del current_path[-1]


def main():

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    required_sum = 23
    print("Tree paths with required_sum " + str(required_sum) +
          ": " + str(find_paths(root, required_sum)))


main()
