# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
# Grokking
# Leetcode https://leetcode.com/problems/number-of-islands/
# Solution https://leetcode.com/problems/number-of-islands/solution/
# Time Complexity O(N+E), where N is the number of nodes in the graph, and E is the number of edges. We explore each node once when we transform it from uncolored
# to colored, traversing all its edges in the process.
# Space Complexity O(N), the space used to store the color.


from typing import List
from collections import defaultdict


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}
        adj_graph = defaultdict(list)
        counter = 0
        for nodes in graph:
            for node in nodes:
                adj_graph[counter].append(node)
                adj_graph[node].append(counter)
            counter += 1

        for node in adj_graph:
            if node not in color:
                stack = [node]
                color[node] = 0
                while stack:
                    node = stack.pop()
                    for neighbor in adj_graph[node]:
                        if neighbor not in color:
                            stack.append(neighbor)
                            color[neighbor] = color[node] ^ 1
                        elif color[neighbor] == color[node]:
                            return False
        return True


sol = Solution()
print(sol.isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]))
print(sol.isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]]))
