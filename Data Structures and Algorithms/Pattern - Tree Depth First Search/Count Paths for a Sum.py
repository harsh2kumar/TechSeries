# Given a binary tree and a number ‘S’, find all paths in the tree such that the sum of all the node values of each path equals ‘S’.
# Please note that the paths can start or end at any node but all paths must follow direction from parent to child (top to bottom).
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/xV2J7jvN1or
# Leetcode https://leetcode.com/problems/path-sum-iii/
# Solution https://leetcode.com/problems/path-sum-iii/solution/
# Time Complexity The time complexity of the above algorithm is O(N^2) in the worst case. The best case of our algorithm will be O(NlogN).
# Space Complexity The space complexity of the above algorithm will be O(N) in the worst case. This space will be used to store the recursion stack.
# The worst case will happen when the given tree is a linked list (i.e., every node has only one child).

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_paths(root, target_sum):
    return count_paths_recursive(root, target_sum, [])


def count_paths_recursive(current_node, target_sum, current_path):
    # check if current node exists
    if not current_node:
        return 0
    # add current_node to current path
    current_path.append(current_node.val)
    # check if any sub-path achieves target sum
    path_count, path_sum = 0, 0
    for i in range(len(current_path)-1, -1, -1):
        path_sum += current_path[i]
        if path_sum == target_sum:
            path_count += 1
    # traverse left-subtree
    path_count += count_paths_recursive(current_node.left,
                                        target_sum, current_path)
    # traverse right-subtree
    path_count += count_paths_recursive(current_node.right,
                                        target_sum, current_path)

    # delete current node to backtrack
    del current_path[-1]

    return path_count


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has paths: " + str(count_paths(root, 11)))


main()
