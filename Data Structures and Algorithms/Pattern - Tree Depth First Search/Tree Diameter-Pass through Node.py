# Given a binary tree, find the length of its diameter. The diameter of a tree is the number of nodes on the longest path between any two leaf nodes.
# The diameter of a tree may or may not pass through the root.
# Note: You can always assume that there are at least two leaf nodes in the given tree.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/JYVW7l2L4EJ
# Leetcode
# Solution
# Time Complexity The time complexity of the above algorithm is O(N), where ‘N’ is the total number of nodes in the tree.
# This is due to the fact that we traverse each node once.
# Space Complexity The space complexity of the above algorithm will be O(N) in the worst case. This space will be used to store the recursion stack.
# The worst case will happen when the given tree is a linked list (i.e., every node has only one child).

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeDiameter:

    def __init__(self):
        self.tree_diameter = 0

    def find_diameter(self, root):
        self.calculate_height(root)
        return self.tree_diameter

    def calculate_height(self, current_node):
        if not current_node:
            return 0

        # if the current node doesn't have a left or right subtree, we can't have
        # a path passing through it, since we need a leaf node on each side
        left_tree_height = self.calculate_height(current_node.left)
        right_tree_height = self.calculate_height(current_node.right)

        # update the global tree diameter
        if left_tree_height and right_tree_height:
            # diameter at the current node will be equal to the height of left subtree +
            # the height of right sub-trees + '1' for the current node
            self.tree_diameter = max(
                self.tree_diameter, left_tree_height+right_tree_height+1)

        # height of the current node will be equal to the maximum of the heights of
        # left or right subtrees plus '1' for the current node
        return max(left_tree_height, right_tree_height)+1


def main():
    treeDiameter = TreeDiameter()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))
    treeDiameter = TreeDiameter()
    root.left.left = None
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.right.left = TreeNode(9)
    root.right.left.right.left = TreeNode(10)
    root.right.right.left.left = TreeNode(11)
    print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))


main()
