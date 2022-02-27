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
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        # board reverse to easily calculate the positions from square to (r, c)
        board.reverse()
        length = len(board)

        def intToPos(square):
            row = (square-1)//length
            col = (square-1) % length  # only valid for even rows
            if row % 2:  # for odd rows
                col = length-1-col
            return row, col

        # Apply BFS approach to find the shortest path
        queue = deque()
        queue.append((1, 0))  # [square, moves]
        visited = set()  # set to maintain unique visited nodes
        while queue:
            square, moves = queue.popleft()
            # roll the dice and go to next square
            for i in range(1, 7):
                next_square = square + i
                r, c = intToPos(next_square)
                if board[r][c] != -1:
                    next_square = board[r][c]
                # if we reach the end, we have found the solution
                if next_square == length*length:
                    return moves + 1
                if next_square not in visited:
                    queue.append((next_square, moves+1))
                    visited.add(next_square)
        # if destination is not reachable return -1
        return -1


sol = Solution()
print("[[-1,-1,19,10,-1],[2,-1,-1,6,-1],[-1,17,-1,19,-1],[25,-1,20,-1,-1],[-1,-1,-1,-1,15]]: ", sol.snakesAndLadders(
    [[-1, -1, 19, 10, -1], [2, -1, -1, 6, -1], [-1, 17, -1, 19, -1], [25, -1, 20, -1, -1], [-1, -1, -1, -1, 15]]))
print("[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]: ", sol.snakesAndLadders(
    [[-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1],
        [-1, 35, -1, -1, 13, -1], [-1, -1, -1, -1, -1, -1], [-1, 15, -1, -1, -1, -1]]
))
print("[[-1,-1],[-1,3]]: ", sol.snakesAndLadders([[-1, -1], [-1, 3]]))
