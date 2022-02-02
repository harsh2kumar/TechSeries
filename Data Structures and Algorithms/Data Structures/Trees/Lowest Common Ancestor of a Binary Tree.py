# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
# Grokking
# Leetcode https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# Solution https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/
# Time Complexity  O(N), where N is the number of nodes in the binary tree. In the worst case we might be visiting all the nodes of the binary tree.
# Space Complexity O(N). This is because the maximum amount of space utilized by the recursion stack would be N since the height of a skewed binary tree could be N.


from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def recurse(current_node):
            if not current_node:
                return False
            # left recursion
            left = recurse(current_node.left)
            # right recursion
            right = recurse(current_node.right)
            mid = current_node == p or current_node == q

            if left+right+mid >= 2:
                self.ans = current_node

            return left or right or mid
        recurse(root)
        return self.ans
