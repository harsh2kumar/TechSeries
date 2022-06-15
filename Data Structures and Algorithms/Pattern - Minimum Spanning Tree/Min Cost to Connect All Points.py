# You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi]. Return the minimum cost to make
# all points connected. All points are connected if there is exactly one simple path between any two points.
# Grokking
# Leetcode https://leetcode.com/problems/min-cost-to-connect-all-points/
# Solution https://leetcode.com/problems/min-cost-to-connect-all-points/solution/
# Time Complexity O(n^2 * log(n)).
# Space Complexity O(n^2).

from heapq import *
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        # adjacency list to maintain cost(distance) of each point from every other point
        adj = {i: [] for i in range(n)}

        # calculate distance for each point
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                # calculate manhattan distance
                x2, y2 = points[j]
                distance = abs(x1-x2)+abs(y1-y2)
                adj[i].append((distance, j))
                adj[j].append((distance, i))

        # Prim's algorithm
        res = 0
        visited = set()
        min_cost = [(0, 0)]  # start with cost 0 and with point 0
        while len(visited) < n:
            cost, node = heappop(min_cost)
            if node in visited:
                continue
            res += cost
            visited.add(node)
            for neighbor_cost, neighbor in adj[node]:
                if neighbor not in visited:
                    heappush(min_cost, (neighbor_cost, neighbor))

        return res


sol = Solution()
print("[[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]: ",
      sol.minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]))
print("[[3, 12], [-2, 5], [-4, 1]]: ",
      sol.minCostConnectPoints([[3, 12], [-2, 5], [-4, 1]]))
