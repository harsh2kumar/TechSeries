# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
# Grokking
# Leetcode https://leetcode.com/problems/subtree-of-another-tree/
# Solution https://leetcode.com/problems/subtree-of-another-tree/solution/
# Time Complexity The runtime complexity of this solution is linear, O(m*n), where m and n are the number of nodes in root and subroot tree respectively.
# Space Complexity The space complexity of this solution is O(h). The recursive solution has O(h) memory complexity as it will consume memory on
# the stack up to the height of binary tree h. It will be O(log n) for a balanced tree and, in the worst case, can be O(n).


from typing import Optional
from BinaryTree import *


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # if subRoot is null, its a subtree of any leaf node of root
        if not subRoot:
            return True
        if not root:
            return False

        if self.sameTree(root, subRoot):
            return True

        # check if subRoot is a subtree of left or right subtree
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

    def sameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if p and q and p.val == q.val:
            return (self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right))
        return False


sol = Solution()
arr1 = [100, 50, 200, 25, 125, 350]
arr2 = [1, 2, 10, 50, 180, 199]
root1 = create_BST(arr1)
root2 = create_BST(arr2)

if(sol.isSubtree(root1, root2)):
    print("Subtree present")
else:
    print("Subtree not present")
