# Design an algorithm to encode an N-ary tree into a binary tree and decode the binary tree to get the original N-ary tree.
# Grokking https://www.educative.io/module/lesson/data-structures-in-python/JP7nxVzLZN9
# Leetcode https://leetcode.com/problems/encode-n-ary-tree-to-binary-tree/
# Solution https://leetcode.com/problems/encode-n-ary-tree-to-binary-tree/solution/
# Time Complexity The runtime complexity of this solution is linear, O(n).
# Space Complexity O(L) where L is the maximum number of nodes that reside at the same level. Since L is proportional to N in the worst case, we could further
# generalize the time complexity to O(N).

from typing import Optional
from collections import deque

# Definition for a Node.


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Optional[Node]') -> Optional[TreeNode]:
        if not root:
            return None
        queue = deque()
        root_b_node = TreeNode(root.val)
        queue.append((root_b_node, root))
        while queue:
            # find parent in b_tree and current node in given n-ary tree
            parent, curr = queue.popleft()
            prev_b_node = None  # for connecting siblings
            head_b_node = None  # for storing first node of all children
            # traverse each child one by one
            for child in curr.children:
                new_b_node = TreeNode(child.val)
                if prev_b_node:
                    prev_b_node.right = new_b_node
                else:
                    head_b_node = new_b_node
                prev_b_node = new_b_node
                queue.append((new_b_node, child))
            # connect parent.left to first child node
            parent.left = head_b_node
        return root_b_node

        # Decodes your binary tree to an n-ary tree.
    def decode(self, data: Optional[TreeNode]) -> 'Optional[Node]':
        if not data:
            return None

        # set as [] instead of None for the online judge to pass
        root_n_node = Node(data.val, [])
        queue = deque()
        queue.append((root_n_node, data))

        while queue:
            parent, curr = queue.popleft()
            first_child = curr.left
            siblings = first_child

            while siblings:
                new_n_node = Node(siblings.val, [])
                parent.children.append(new_n_node)
                queue.append((new_n_node, siblings))
                siblings = siblings.right
        return root_n_node

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))
