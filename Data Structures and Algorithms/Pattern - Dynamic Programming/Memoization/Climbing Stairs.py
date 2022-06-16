# You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to
# the top?
# Grokking
# Leetcode https://leetcode.com/problems/climbing-stairs/
# Solution https://leetcode.com/problems/climbing-stairs/solution/
# Time Complexity The time complexity of the above algorithm is O(n).
# Space Complexity The space complexity of this algorithm is O(1).


class Solution:
    def climbStairs(self, n: int) -> int:
        # base case
        # if we are on last stair, then there is 1 way to reach the destination, by not moving at all
        # if we are on the second-last stair, then there is 1 way to reach the destination, by taking one step and reaching the last stair
        one, two = 1, 1
        # everytime, we just compute the results by adding results from the next 2 steps
        for _ in range(n-1):
            temp = one
            one = one+two
            two = temp
        # return the answer
        return one


sol = Solution()
print("2: ", sol.climbStairs(2))
print("3: ", sol.climbStairs(3))
print("5: ", sol.climbStairs(5))
