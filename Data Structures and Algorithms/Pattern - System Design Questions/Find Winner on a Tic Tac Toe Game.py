# Implement the TicTacToe class. You can assume that moves is valid (i.e., it follows the rules of Tic-Tac-Toe), the grid is initially empty, and A will play first.
# Grokking
# Leetcode https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/
# Solution https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/solution/
# Time Complexity  O(1) because for every move, we mark a particular row, column, diagonal, and anti-diagonal in constant time.
# Space Complexity O(n) because we use arrays rows and cols of size n. The variables diagonal and antiDiagonal use constant extra space.


from typing import List


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:

        # n stands for the size of the board, n = 3 for the current game.
        n = 3

        # use rows and cols to record the value on each row and each column.
        # diag1 and diag2 to record value on diagonal or anti-diagonal.
        rows, cols = [0] * n, [0] * n
        diag = anti_diag = 0

        # Two players having value of 1 and -1, player_1 with value = 1 places first.
        player = 1

        for row, col in moves:

            # Update the row value and column value.
            rows[row] += player
            cols[col] += player

            # If this move is placed on diagonal or anti-diagonal,
            # we shall update the relative value as well.
            if row == col:
                diag += player
            if row + col == n - 1:
                anti_diag += player

            # check if this move meets any of the winning conditions.
            if any(abs(line) == n for line in (rows[row], cols[col], diag, anti_diag)):
                return "A" if player == 1 else "B"

            # If no one wins so far, change to the other player alternatively.
            # That is from 1 to -1, from -1 to 1.
            player *= -1

        # If all moves are completed and there is still no result, we shall check if
        # the grid is full or not. If so, the game ends with draw, otherwise pending.
        return "Draw" if len(moves) == n * n else "Pending"


sol = Solution()
moves = [[[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]],
         [[0, 0], [1, 1], [0, 1], [0, 2], [1, 0], [2, 0]],
         [[0, 0], [1, 1], [2, 0], [1, 0], [1, 2], [2, 1], [0, 1], [0, 2], [2, 2]]]
for move in moves:
    print(sol.tictactoe(move))
