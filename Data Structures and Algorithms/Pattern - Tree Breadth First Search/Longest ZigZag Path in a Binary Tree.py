# You are given the root of a binary tree. Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).
# Return the longest ZigZag path contained in that tree.
# Grokking
# Leetcode https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/
# Solution https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/solution/
# Time Complexity The time complexity of the above algorithm is O(N), where ‘N’ is the total number of nodes in the tree.
# This is due to the fact that we traverse each node once.
# Space Complexity The space complexity of the above algorithm will be O(N) as we need to return a list containing the level order traversal.
# We will also need O(N) space for the queue. Since we can have a maximum of N/2 nodes at any level (this could happen only at the lowest level),
# therefore we will need O(N) space to store them in the queue.

from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    ## iterative
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        result = 0
        if not root:
            return result
        queue = deque()  # triple(node, is_left, depth)
        if root.left:
            queue.append((root.left, True, 1))
        if root.right:
            queue.append((root.right, False, 1))

        while queue:
            node, is_left, depth = queue.popleft()
            result = max(result, depth)
            if is_left:
                if node.right:
                    queue.append((node.right, False, depth+1))
                if node.left:
                    queue.append((node.left, True, 1))
            else:
                if node.left:
                    queue.append((node.left, True, depth+1))
                if node.right:
                    queue.append((node.right, False, 1))
        return result
    
    ## recursive
    def longestZigZagRecursive(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.dfs(root.left, True, 1)
        self.dfs(root.right, False, 1)
        return self.res

    def dfs(self, node, isLeft, depth):
        if not node:
            return
        self.res = max(self.res, depth)

        if isLeft:
            self.dfs(node.left, True, 1)
            self.dfs(node.right, False, depth+1)
        else:
            self.dfs(node.left, True, depth+1)
            self.dfs(node.right, False, 1)
