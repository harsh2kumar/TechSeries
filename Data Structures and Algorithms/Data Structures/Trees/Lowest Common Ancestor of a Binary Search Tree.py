# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
# Grokking
# Leetcode https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# Solution https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/solution/
# Time Complexity  O(N), where N is the number of nodes in the binary tree. In the worst case we might be visiting all the nodes of the binary tree.
# Space Complexity O(N). This is because the maximum amount of space utilized by the recursion stack would be N since the height of a skewed binary tree could be N.


from typing import List
from BinaryTree import *

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # Value of current node or parent node.
        parent_val = root.val

        # Value of p
        p_val = p.val

        # Value of q
        q_val = q.val

        # If both p and q are greater than parent
        if p_val > parent_val and q_val > parent_val:
            return self.lowestCommonAncestor(root.right, p, q)
        # If both p and q are lesser than parent
        elif p_val < parent_val and q_val < parent_val:
            return self.lowestCommonAncestor(root.left, p, q)
        # We have found the split point, i.e. the LCA node.
        else:
            return root


sol = Solution()

arr = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
p, q = BinaryTreeNode(2), BinaryTreeNode(8)
root = create_BST(arr)
print("LCA of ", p.val, " and ", q.val, " is ",
      sol.lowestCommonAncestor(root, p, q).val)

arr = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
p, q = BinaryTreeNode(2), BinaryTreeNode(4)
root = create_BST(arr)
print("LCA of ", p.val, " and ", q.val, " is ",
      sol.lowestCommonAncestor(root, p, q).val)

arr = [2, 1]
p, q = BinaryTreeNode(2), BinaryTreeNode(1)
root = create_BST(arr)
print("LCA of ", p.val, " and ", q.val, " is ",
      sol.lowestCommonAncestor(root, p, q).val)
