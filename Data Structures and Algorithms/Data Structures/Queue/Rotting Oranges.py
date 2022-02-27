# You are given an m x n grid where each cell can have one of three values. Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes
# rotten. Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
# Grokking
# Leetcode https://leetcode.com/problems/rotting-oranges/
# Solution https://leetcode.com/problems/rotting-oranges/solution/
# Time Complexity O(N), where N is the size of the grid.
# Space Complexity O(N), where N is the size of the grid.


from collections import deque
from os import getgrouplist, getpriority
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()

        ROWS, COLS = len(grid), len(grid[0])
        fresh_oranges = 0
        # build the set of rotten oranges
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1
        # mark the round / level
        queue.append((-1, -1))

        # start the rotting process via BFS
        minutes_elapsed = -1
        # Up, Down, Left, Right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            row, col = queue.popleft()
            # we finished one round of processing
            if row == -1:
                minutes_elapsed += 1
                if queue:  # to avoid the endless loop
                    queue.append((-1, -1))
            else:
                # this is a rotten orange
                # it would contaminate its neighbors
                for d in directions:
                    neighbor_row, neighbor_col = row+d[0], col+d[1]
                    if ROWS > neighbor_row >= 0 and COLS > neighbor_col >= 0:
                        # check if there is a fresh orange
                        if grid[neighbor_row][neighbor_col] == 1:
                            # contaminate the orange
                            grid[neighbor_row][neighbor_col] = 2
                            fresh_oranges -= 1
                            # this orange will contaminate other oranges
                            queue.append((neighbor_row, neighbor_col))
        # return elapsed minutes if no fresh oranges are left
        return minutes_elapsed if fresh_oranges == 0 else -1


sol = Solution()
print("[[2,1,1],[1,1,0],[0,1,1]]: ", sol.orangesRotting(
    [[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
print("[[2,1,1],[0,1,1],[1,0,1]]: ", sol.orangesRotting(
    [[2, 1, 1], [0, 1, 1], [1, 0, 1]]))
print("[[0,2]]: ", sol.orangesRotting([[0, 2]]))
