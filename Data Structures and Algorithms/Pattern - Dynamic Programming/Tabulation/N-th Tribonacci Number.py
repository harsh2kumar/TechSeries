# The Tribonacci sequence Tn is defined as follows: T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0. Given n, return the value of Tn.
# Grokking
# Leetcode https://leetcode.com/problems/n-th-tribonacci-number/
# Solution https://leetcode.com/problems/n-th-tribonacci-number/solution/
# Time Complexity The time complexity of this algorithm is O(1).
# Space Complexity The space complexity of this algorithm is O(1).


class Solution:
    def __init__(self):
        self.tri = [0]*38
        self.tri[0] = 0
        self.tri[1] = 1
        self.tri[2] = 1
        for i in range(3, len(self.tri)):
            self.tri[i] = self.tri[i-1]+self.tri[i-2]+self.tri[i-3]

    def tribonacci(self, n: int) -> int:
        return self.tri[n]


sol = Solution()
print("4: ", sol.tribonacci(4))
print("25: ", sol.tribonacci(25))
