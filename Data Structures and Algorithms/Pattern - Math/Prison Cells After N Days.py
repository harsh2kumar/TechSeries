# There are 8 prison cells in a row and each cell is either occupied or vacant.
# Each day, whether the cell is occupied or vacant changes according to the following rules:
# If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
# Otherwise, it becomes vacant.
# Return the state of the prison after n days (i.e., n such changes described above).
# Grokking
# Leetcode https://leetcode.com/problems/prison-cells-after-n-days/
# Solution https://leetcode.com/problems/prison-cells-after-n-days/solution/
# Time Complexity  O(K⋅min(N,2^K))
# Space Complexity The space complexity is O(K⋅2^K).

from typing import List


class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        has_cycle = False
        arrangements = set()
        days = 0
        for i in range(n):
            next = self.get_next(cells)
            if str(next) in arrangements:
                has_cycle = True
                break
            else:
                days += 1
            cells = next
        if has_cycle:
            n %= days
            for i in range(n):
                cells = self.get_next(cells)
        return cells

    def get_next(self, cells):
        N = len(cells)
        next = [0]*N
        for i in range(N):
            if i == 0 or i == N-1:
                next[i] = 0
            else:
                next[i] = 1 if cells[i-1] == cells[i+1] else 0
        return next


sol = Solution()
print("[0,1,0,1,1,0,0,1], 7: ", sol.prisonAfterNDays(
    [0, 1, 0, 1, 1, 0, 0, 1], 7))
