# You are starving and you want to eat food as quickly as possible. You want to find the shortest path to arrive at any food cell. Return the length of the shortest
# path for you to reach any food cell. If there is no path for you to reach food, return -1.
# Grokking
# Leetcode https://leetcode.com/problems/shortest-path-to-get-food/
# Solution https://leetcode.com/problems/shortest-path-to-get-food/solution/
# Time Complexity The time complexity of the above algorithm is $O(M.N), where ‘M’ & ‘N’ are the total number of cells in the grid. This is due to the fact that
# we traverse each cell once.
# Space Complexity The space complexity of the above algorithm will be O(M.N) as we need to return a list containing the level order traversal. We will also need
# O(M.N) space for the queue. Since we can have a maximum of M.N/2 nodes at any level (this could happen only at the lowest level), therefore we will need 
# O(M.N) space to store them in the queue.

from collections import deque
from typing import List


class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        # we will use queue based approach here
        rows = len(grid)
        cols = len(grid[0])

        # initialize the queue with starting location
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "*":
                    # triple(row, col, distance to food)
                    queue.append((r, c, 0))

        # Up, Down, Left, Right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            row, col, distance = queue.popleft()
            for d in directions:
                next_r, next_c = row+d[0], col+d[1]
                # check if its a valid move
                if 0 <= next_r < rows and 0 <= next_c < cols and grid[next_r][next_c] != "X":
                    # if its a food cell return distance+1
                    if grid[next_r][next_c] == "#":
                        return distance+1
                    else:
                        # mark the current cell as visited
                        grid[next_r][next_c] = "X"
                        # add next possible move to the queue
                        queue.append((next_r, next_c, distance+1))
        # if food cell wasn't found return -1
        return -1


sol = Solution()
print(sol.getFood([["X", "X", "X", "X", "X", "X"], ["X", "*", "O", "O", "O",
      "X"], ["X", "O", "O", "#", "O", "X"], ["X", "X", "X", "X", "X", "X"]]))
print(sol.getFood([["X", "X", "X", "X", "X"], ["X", "*", "X", "O",
      "X"], ["X", "O", "X", "#", "X"], ["X", "X", "X", "X", "X"]]))
print(sol.getFood([["X", "X", "X", "X", "X", "X", "X", "X"], ["X", "*", "O", "X", "O", "#", "O", "X"], ["X", "O",
      "O", "X", "O", "O", "X", "X"], ["X", "O", "O", "O", "O", "#", "O", "X"], ["X", "X", "X", "X", "X", "X", "X", "X"]]))
