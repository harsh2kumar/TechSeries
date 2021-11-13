# Given a binary tree, return all root-to-leaf paths.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/B815A0y2Ajn
# Leetcode https://leetcode.com/problems/binary-tree-paths/
# Solution https://leetcode.com/problems/binary-tree-paths/solution/
# Time Complexity The time complexity of the above algorithm is O(N^2)
# Space Complexity Tour algorithm’s overall space complexity is O(N*logN).

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_paths(root):
    all_paths = []
    find_paths_recursive(root, [], all_paths)
    return all_paths


def find_paths_recursive(current_node, current_path, all_paths):
    if current_node is None:
        return

    # add the current node to the path
    current_path.append(current_node.val)

    # if the current node is a leaf, save the current path
    if current_node.left is None and current_node.right is None:
        all_paths.append(list(current_path))
    else:
        # traverse the left sub-tree
        find_paths_recursive(current_node.left, current_path, all_paths)
        # traverse the right sub-tree
        find_paths_recursive(current_node.right, current_path, all_paths)

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
    print("All paths for Binary Tree : " + str(find_paths(root)))


main()
