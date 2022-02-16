# Implement the TicTacToe class.
# Grokking
# Leetcode https://leetcode.com/problems/design-tic-tac-toe/
# Solution https://leetcode.com/problems/design-tic-tac-toe/solution/
# Time Complexity  O(1) because for every move, we mark a particular row, column, diagonal, and anti-diagonal in constant time.
# Space Complexity O(n) because we use arrays rows and cols of size n. The variables diagonal and antiDiagonal use constant extra space.


from typing import List


class TicTacToe:

    def __init__(self, n: int):
        self.rows = [0]*n
        self.cols = [0]*n
        self.diagonal, self.anti_diagonal = 0, 0

    def move(self, row: int, col: int, player: int) -> int:
        size = len(self.rows)
        current_player_weight = 1 if player == 1 else -1
        self.rows[row] += current_player_weight
        self.cols[col] += current_player_weight
        if row == col:
            self.diagonal += current_player_weight
        if row == (len(self.rows)-col-1):
            self.anti_diagonal += current_player_weight

        # check if current player is winning
        # print(abs(self.rows[row]))
        # print(abs(self.cols[col]))
        # print(abs(self.diagonal))
        # print(abs(self.anti_diagonal))
        if abs(self.rows[row]) == size or abs(self.cols[col]) == size or abs(self.diagonal) == size or abs(self.anti_diagonal) == size:
            return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)

# ["TicTacToe","move","move","move","move","move","move","move"]
# [[3],[0,0,1],[0,2,2],[2,2,1],[1,1,2],[2,0,1],[1,0,2],[2,1,1]]

print("Initialize Board")
sol = TicTacToe(3)
moves = [[0, 0, 1], [0, 2, 2], [2, 2, 1], [
    1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]]
print("Make moves")
for move in moves:
    print(sol.move(move[0], move[1], move[2]))
