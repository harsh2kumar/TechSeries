# Given an array of distinct integers candidates and a target integer target, return a boolean indicating whether it is possible to choose numbers that
# sum to target. The same number may be chosen from candidates an unlimited number of times.
# Two combinations are unique if the frequency of at least one of the chosen numbers is different.
# It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
# Grokking
# Leetcode https://leetcode.com/problems/combination-sum/
# Solution https://leetcode.com/problems/combination-sum/solution/
# Time Complexity The time complexity of the above algorithm is O(m*n).
# Space Complexity The space complexity of this algorithm is O(m+n).


from math import remainder
from typing import List


class Solution:
    def __init__(self) -> None:
        self.memo = {}

    def howSum(self, targetSum: int, nums: List, memo={}) -> List[int]:
        if targetSum in self.memo:
            return self.memo[targetSum]
        if targetSum == 0:
            return []
        if targetSum < 0:
            return None
        for num in nums:
            remainder = targetSum-num
            # print("--", num, remainder)
            remainder_result = self.howSum(remainder, nums, memo)
            # print("++", remainder_result)
            if remainder_result != None:
                memo[targetSum] = [*remainder_result, num]
                # print(memo[targetSum])
                return memo[targetSum]
        self.memo[targetSum] = None
        return None


sol = Solution()
print("7, [2, 3]: ", sol.howSum(7, [2, 3]))
sol = Solution()
print("7, [5, 3, 4, 7]: ", sol.howSum(7, [5, 3, 4, 7]))
sol = Solution()
print("7, [2, 4]: ", sol.howSum(7, [2, 4]))
sol = Solution()
print("8, [2, 3, 5]: ", sol.howSum(8, [2, 3, 5]))
sol = Solution()
print("300, [7, 14]: ", sol.howSum(300, [7, 14]))
sol = Solution()
print("300, [10]: ", sol.howSum(300, [10]))
