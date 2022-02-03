# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
# Grokking
# Leetcode https://leetcode.com/problems/word-search/
# Solution https://leetcode.com/problems/word-search/solution/
# Time Complexity O(N⋅3^L) where N is the number of cells in the board and L is the length of the word to be matched.
# Space Complexity O(L) where L is the length of the word to be matched.


from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.ROWS = len(board)
        self.COLS = len(board[0])
        self.board = board

        for row in range(self.ROWS):
            for col in range(self.COLS):
                # exact word match found
                if self.backtrack(row, col, word):
                    return True
        # match not found
        return False

    def backtrack(self, row, col, suffix):
        # if all letters matched, return True
        if len(suffix) == 0:
            return True

        # check False conditions
        if row < 0 or row == self.ROWS or col < 0 or col == self.COLS or self.board[row][col] != suffix[0]:
            return False
        # initialize return value as False
        # WEIRD: if ret was defined after self.board set as #, I get TLE
        ret = False
        # mark the current word
        self.board[row][col] = "#"
        for row_offset, col_offset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ret = self.backtrack(row+row_offset, col+col_offset, suffix[1:])
            if ret:
                break

        # unmark current cell
        self.board[row][col] = suffix[0]

        # retun result
        return ret


sol = Solution()
print(sol.exist([["A", "B", "C", "E"], [
      "S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"))
print(sol.exist([["A", "B", "C", "E"], [
      "S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"))
print(sol.exist([["A", "B", "C", "E"], [
      "S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"))
