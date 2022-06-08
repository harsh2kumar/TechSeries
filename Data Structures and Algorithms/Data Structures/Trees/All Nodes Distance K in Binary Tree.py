# Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k
# from the target node. You can return the answer in any order.
# Grokking
# Leetcode https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
# Solution https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/solution/
# Time Complexity The runtime complexity of this solution is O(m^2*n) where m is the size of word and n is total number of words.
# Space Complexity The space complexity of this solution is O(m^2*n) where m is the size of word and n is total number of words.


from collections import defaultdict, deque
from typing import List
from BinaryTree import *


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # convert node into a bidirectional graph
        graph = defaultdict(list)
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
                graph[node].append(node.left)
                graph[node.left].append(node)

            if node.right:
                queue.append(node.right)
                graph[node].append(node.right)
                graph[node.right].append(node)

        # search for all distance K nodes from target node using BFS
        target_queue = deque([target])
        result = []
        visited = set([target])
        distance = 0
        while target_queue and distance <= k:
            level_size = len(target_queue)
            for _ in range(level_size):
                node = target_queue.popleft()
                if distance == k:
                    result.append(node.val)
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        target_queue.append(neighbor)
                        visited.add(neighbor)
            distance += 1
        return result


arr1 = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
arr2 = [1]
root1 = create_BST(arr1)
root2 = create_BST(arr2)

sol = Solution()
print(sol.distanceK(root1, TreeNode(5), 2))
print(sol.distanceK(root2, TreeNode(1), 3))
