# We are given an array asteroids of integers representing asteroids in a row. For each asteroid, the absolute value represents its size, and the sign represents
# its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed. Find out the state of the asteroids after all collisions.
# If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.
# Grokking
# Leetcode https://leetcode.com/problems/asteroid-collision/
# Solution https://leetcode.com/problems/asteroid-collision/solution/
# Time Complexity O(N), where N is the number of asteroids. Our stack pushes and pops each asteroid at most once.
# Space Complexity O(N). We use a stack to keep track of the intermediate results. In the worst case, the states do not evolve at the end, i.e. we need O(N)
# space where N is the number of input asteroids.


from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ast in asteroids:
            # collision ONLY occurs if new asteroid is moving left and top is moving right
            while stack and ast < 0 < stack[-1]:
                if stack[-1] < -ast:
                    stack.pop()
                    continue
                # break if both asteroids are equal
                elif stack[-1] == -ast:
                    stack.pop()
                break
            else:
                stack.append(ast)
        return stack


sol = Solution()
print(sol.asteroidCollision([5, 10, -5]))
print(sol.asteroidCollision([8, -8]))
print(sol.asteroidCollision([10, 2, -5]))
