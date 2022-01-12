# We are given a Binary Search Tree(BST) and a node number nn. We have to find the node with the nth highest value.
# Grokking https://www.educative.io/module/lesson/data-structures-in-python/qZO8y7mxAVr
# Leetcode https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Solution https://leetcode.com/problems/kth-smallest-element-in-a-bst/solution/
# Time Complexity The runtime complexity of this solution is linear, O(n).
# Space Complexity The memory complexity of this solution is O(h). An iterative solution has O(h) memory complexity as it instantiates a stack
# that has to store information up to the height of the binary tree (h). It will be O(logn) for a balanced tree and, in the worst case, can be O(n).

from BinaryTree import *
from typing import Optional


class Solution:
    def __init__(self):
        self.seen_nodes = 0

    def kthHighest(self, root: Optional[BinaryTreeNode], k: int) -> int:
        # since BSTs in-order traversal gives us a sorted list
        # perform reverse in-order traversal and count the number of seen nodes
        # kth node seen will be the highest
        if not root:
            return None
        res = self.kthHighest(root.right, k)
        if res != None:
            return res
        self.seen_nodes += 1
        if self.seen_nodes == k:
            return root
        res = self.kthHighest(root.left, k)
        if res != None:
            return res
        return None


arr = [100, 50, 200, 25, 75, 125, 350]
root = create_BST(arr)

print("Level Order Traversal:")
display_level_order(root)

sol = Solution()
n = 2
current_count = 0
nth_highest_node = sol.kthHighest(root, n)
print(str(nth_highest_node.data))

sol = Solution()
n = 1
current_count = 0
nth_highest_node = sol.kthHighest(root, n)
print(str(nth_highest_node.data))

sol = Solution()
n = 5
current_count = 0
nth_highest_node = sol.kthHighest(root, n)
print(str(nth_highest_node.data))

sol = Solution()
n = 30
current_count = 0
nth_highest_node = sol.kthHighest(root, n)
print(str(nth_highest_node))
