# Given a binary tree and a number sequence, find if the sequence is present as a root-to-leaf path in the given tree.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/m280XNlPOkn
# Leetcode https://leetcode.com/problems/check-if-a-string-is-a-valid-sequence-from-root-to-leaves-path-in-a-binary-tree/
# Solution https://leetcode.com/problems/check-if-a-string-is-a-valid-sequence-from-root-to-leaves-path-in-a-binary-tree/solution/
# Time Complexity The time complexity of the above algorithm is O(N), where ‘N’ is the total number of nodes in the tree.
# This is due to the fact that we traverse each node once.
# Space Complexity The space complexity of the above algorithm will be O(N) in the worst case. This space will be used to store the recursion stack.
# The worst case will happen when the given tree is a linked list (i.e., every node has only one child).

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_path(root, sequence):
    if not root:
        return len(sequence) == 0
    return find_path_recursive(root, sequence, 0)


def find_path_recursive(current_node, sequence, sequence_index):
    # check if current node exists
    if not current_node:
        return False
    # check if sequence_index is greater than sequence length or if there is a character mismatch
    if sequence_index >= len(sequence) or current_node.val != sequence[sequence_index]:
        return False
    # check if current node is a leaf node
    # and if this is the last character of our sequence
    if not current_node.left and not current_node.right and sequence_index == len(sequence)-1:
        return True
    return find_path_recursive(current_node.left, sequence, sequence_index+1) or find_path_recursive(current_node.right, sequence, sequence_index+1)


def main():

    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)

    print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
    print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


main()
