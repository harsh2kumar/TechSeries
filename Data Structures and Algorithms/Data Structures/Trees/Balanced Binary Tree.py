# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
# Grokking
# Leetcode https://leetcode.com/problems/symmetric-tree/
# Solution https://leetcode.com/problems/symmetric-tree/solution/
# Time Complexity The runtime complexity of this solution is linear, O(n).
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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root:
                return [True, 0]
            left, right = dfs(root.left), dfs(root.right)

            balanced = left[0] and right[0] and abs(left[1]-right[1]) < 2

            return [balanced, 1+max(left[1], right[1])]

        return dfs(root)[0]


sol = Solution()

arr1 = [3, 9, 20, None, None, 15, 7]
root1 = create_BST(arr1)
if(sol.isBalanced(root1)):
    print("The tree is balanced")
else:
    print("The tree is not balanced")

arr2 = [1, 2, 2, 3, 3, None, None, 4, 4]
root2 = create_BST(arr2)
if(sol.isBalanced(root2)):
    print("The tree is balanced")
else:
    print("The tree is not balanced")

arr3 = []
root3 = create_BST(arr3)
if(sol.isBalanced(root3)):
    print("The tree is balanced")
else:
    print("The tree is not balanced")
